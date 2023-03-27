from django.db.models import Q

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

from .models import Group
from .serializers import GroupSerializer
from drf_tsk.permissions import IsOwnerOrReadOnly


class GroupList(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all().order_by('-created_at')
    allowed_methods = ['GET', 'PUT', 'POST', 'PATCH', 'DELETE']

    def get(self, request, *args, **kwargs):
        """Return a list of groups owned by the current user."""
        if request.user.is_anonymous:
            return Response(status=status.HTTP_404_NOT_FOUND)
        groups = self.get_queryset().filter(
            Q(owner=request.user) | Q(members=request.user)
        ).distinct()
        serializer = self.get_serializer(groups, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    allowed_methods = ['GET', 'PUT', 'POST', 'PATCH', 'DELETE']
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
