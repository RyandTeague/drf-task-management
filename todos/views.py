from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        todo = serializer.instance
        if self.request.user == todo.owner or self.request.user == todo.assigned_to:
            serializer.save()
        else:
            raise permissions.PermissionDenied()
