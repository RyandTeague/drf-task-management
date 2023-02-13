from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class Todo(generics.ListAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer