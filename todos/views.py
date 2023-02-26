from .models import Todo
from .serializers import TodoSerializer
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'deadline',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Todo.objects.all().order_by('-created_at')
"""
    def perform_update(self, serializer):
        todo = serializer.instance
        if self.request.user == todo.owner or self.request.user == todo.assigned_to:
            serializer.save()
        else:
            raise permissions.PermissionDenied()
            """
