from rest_framework import generics, permissions
from drf_tsk.permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import ToDoSerializer

class Todo(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)