from django.contrib.auth.models import User
from datetime import datetime, timedelta
from rest_framework.request import Request
from .models import Todo
from .serializers import TodoSerializer
from django.test import RequestFactory, TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TodoListCreateViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('todo-list-create')
        self.user = User.objects.create(username='testuser')
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'title': 'Test Todo',
            'description': 'This is a test todo',
            'deadline': datetime.now() + timedelta(days=1),
        }

    def test_create_todo_with_invalid_data(self):
        invalid_payload = {'title': ''}
        response = self.client.post(self.url, data=invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class TodoRetrieveUpdateDestroyViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.todo = Todo.objects.create(
            owner=self.user,
            title='Test Todo',
            description='This is a test todo',
            deadline=datetime.now() + timedelta(days=1),
            assigned_to=self.user,
        )
        self.url = reverse('todo-detail', kwargs={'pk': self.todo.id})
        self.client.force_authenticate(user=self.user)
        self.valid_payload = {
            'title': 'Updated Test Todo',
            'description': 'This is an updated test todo',
            'deadline': datetime.now() + timedelta(days=2),
        }

    def test_retrieve_todo(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, TodoSerializer(self.todo).data)

    def test_update_todo_with_invalid_data(self):
        invalid_payload = {'title': ''}
        response = self.client.put(self.url, data=invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_todo(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TodoSerializerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        deadline_str = '2022-01-01'
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        self.todo = Todo.objects.create(
            owner=self.user,
            title='Test Todo',
            overdue=False,
            description='Test description',
            assigned_to=self.user,
            deadline=deadline,
            completed=False
        )
        self.serializer = TodoSerializer(instance=self.todo)

    def test_todo_serializer(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), {'id', 'owner', 'title', 'overdue', 'description', 'assigned_to', 'deadline', 'completed', 'created', 'updated_at'})
        self.assertEqual(data['id'], self.todo.id)
        self.assertEqual(data['owner'], self.user.username)
        self.assertEqual(data['title'], 'Test Todo')
        self.assertEqual(data['overdue'], True)
        self.assertEqual(data['description'], 'Test description')
        self.assertEqual(data['assigned_to'], 1)
        self.assertEqual(data['deadline'], '01 Jan 2022')
        self.assertEqual(data['completed'], False)


class TodoModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.todo = Todo.objects.create(
            owner=self.user,
            title='Test Todo',
            description='This is a test todo',
            deadline=datetime.now() + timedelta(days=1),
            assigned_to=self.user,
        )

    def test_todo_creation(self):
        todo = Todo.objects.create(
            owner=self.user,
            title='New Todo',
            description='This is a new todo',
            deadline=datetime.now() + timedelta(days=2),
            assigned_to=self.user,
        )
        self.assertIsInstance(todo, Todo)
        self.assertEqual(todo.title, 'New Todo')
        self.assertEqual(todo.description, 'This is a new todo')
        self.assertEqual(todo.owner, self.user)
        self.assertFalse(todo.completed)
        self.assertFalse(todo.overdue)

    def test_todo_overdue(self):
        todo = Todo.objects.create(
            owner=self.user,
            title='Overdue Todo',
            description='This is an overdue todo',
            deadline=datetime.now() - timedelta(days=1),
            assigned_to=self.user,
        )
        self.assertTrue(todo.overdue)

    def test_todo_completed(self):
        self.todo.completed = True
        self.todo.save()
        self.assertTrue(self.todo.completed)

    def test_todo_str_method(self):
        self.assertEqual(str(self.todo), f'{self.todo.id} Test Todo')

    def tearDown(self):
        self.user.delete()
        self.todo.delete()
