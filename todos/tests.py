from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Todo
from .serializers import TodoSerializer

class TodoModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.todo = Todo.objects.create(title='Test Todo', owner=self.user)

    def test_todo_creation(self):
        self.assertTrue(isinstance(self.todo, Todo))
        self.assertEqual(str(self.todo), f'{self.todo.id} Test Todo')

    def test_todo_completion(self):
        self.assertFalse(self.todo.completed)
        self.todo.completed = True
        self.assertTrue(self.todo.completed)

    def test_todo_ordering(self):
        todos = Todo.objects.all()
        self.assertEqual(todos[0], self.todo)
        self.assertEqual(todos[0].title, 'Test Todo')
        self.assertEqual(todos[0].created_at.date(), self.todo.created_at.date())

class TodoTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.todo = Todo.objects.create(owner=self.user, title='Test Todo', content='Test content')

    def test_todo_list(self):
        url = reverse('todo-list-create')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_todo(self):
        url = reverse('todo-list-create')
        data = {
            'title': 'Test Todo',
            'content': 'Test content',
            'deadline': '2023-04-01T12:00:00Z',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
