from django.test import TestCase
from django.contrib.auth.models import User
from .models import Todo

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
