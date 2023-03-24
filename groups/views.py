from rest_framework import generics, permissions

from .models import Group
from .serializers import GroupSerializer


class GroupList(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all().order_by('-created_at')
    allowed_methods = None
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    allowed_methods = None
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
