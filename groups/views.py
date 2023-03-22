from rest_framework import generics, permissions

from .models import Group
from .serializers import GroupSerializer


class GroupList(generics.CreateAPIView):
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
