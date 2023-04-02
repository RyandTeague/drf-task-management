from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_tsk.permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer

from commons.utils import get_paginated_response


class TodoListCreateAPIView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, format=None):
		data = request.data
		data['owner'] = request.user.id
		serializer = TodoSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response({'errors': serializer.errors, 'message': "Todo create failed"}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'data': serializer.data, 'message': "Todo created successfully"}, status=status.HTTP_201_CREATED)

	def get(self, request, format=None):
		todos = Todo.objects.filter(owner=request.user, completed=False)
		response = get_paginated_response(request, todos, TodoListSerializer)
		print('response: ', response)
		return Response(response, status=status.HTTP_200_OK)


class TodoRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, pk, format=None):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoListSerializer(todo, context={'request': request})
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({'message': "Requested todo doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'errors': serializer.errors, 'message': "Todo update failed"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'data': serializer.data, 'message': "Todo updated successfully"}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({'message': "Requested todo doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        try:
            todo = Todo.objects.get(pk=pk)
            serializer = TodoSerializer(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response({'errors': serializer.errors, 'message': "Todo updated successfully"}, status=status.HTTP_200_OK)
            return Response({'errors': serializer.errors, 'message': "Todo update failed"}, status=status.HTTP_400_BAD_REQUEST)
        except Todo.DoesNotExist:
            return Response({'message': "Requested todo doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.delete()
            return Response({'message': "Todo deleted successfully"}, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response({'message': "Requested todo doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)












# from .models import Todo
# from .serializers import TodoSerializer
# from django.db.models import Count
# from rest_framework import generics, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from drf_tsk.permissions import IsOwnerOrReadOnly
# from rest_framework.response import Response
# from rest_framework import status


# class TodoList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Todo.objects.filter(completed=False)
#     serializer_class = TodoSerializer

#     filter_backends = [
#         filters.OrderingFilter,
#         filters.SearchFilter,
#         DjangoFilterBackend,
#     ]
#     filterset_fields = [
#         'owner__profile',
#     #    'project'
#     ]
#     search_fields = [
#         'owner__username',
#         'title',
#     #    'project',
#     ]
#     ordering_fields = [
#         'deadline',
#         'created_at',
#         'updated_at',
#     ]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsOwnerOrReadOnly]
#     queryset = Todo.objects.all().order_by('-created_at')
#     serializer_class = TodoSerializer


"""
    def perform_update(self, serializer):
        todo = serializer.instance
        if self.request.user == todo.owner or self.request.user == todo.assigned_to:
            serializer.save()
        else:
            raise permissions.PermissionDenied()
            """
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
"""