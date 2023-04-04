from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
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