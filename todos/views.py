from .models import Todo, Project
from .serializers import TodoSerializer, ProjectSerializer
from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_tsk.permissions import IsOwnerOrReadOnly

class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'owner__profile',
        'project'
    ]
    search_fields = [
        'owner__username',
        'title',
        'project',
    ]
    ordering_fields = [
        'deadline',
        'created_at',
        'updated_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
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

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
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


class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Project.objects.all().order_by('-created_at')