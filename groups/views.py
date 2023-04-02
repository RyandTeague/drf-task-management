from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from django.contrib.auth.models import User

from drf_tsk.permissions import IsOwnerOrReadOnly
from .models import Group
from .serializers import GroupSerializer, GroupListSerializer

from drf_tsk.serializers import UserSerializer

from commons.utils import get_paginated_response


class GroupListCreateAPIView(APIView):
	permission_classes = [IsAuthenticated]

	def post(self, request, format=None):
		data = request.data
		data['owner'] = request.user.id
		serializer = GroupSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		else:
			return Response({'errors': serializer.errors, 'message': "Group create failed"}, status=status.HTTP_400_BAD_REQUEST)
		return Response({'data': serializer.data, 'message': "Group created successfully"}, status=status.HTTP_201_CREATED)

	def get(self, request, format=None):
		groups = Group.objects.filter(Q(owner=request.user)|Q(members=request.user)).distinct()
		response = get_paginated_response(request, groups, GroupListSerializer)
		# print('response: ', response)
		return Response(response, status=status.HTTP_200_OK)


class GroupRetrieveUpdateDestroyAPIView(APIView):
	permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

	def get(self, request, pk, format=None):
		try:
			group = Group.objects.get(pk=pk)
			serializer = GroupListSerializer(group, context={'request': request})
			return Response({'data': serializer.data}, status=status.HTTP_200_OK)
		except Group.DoesNotExist:
			return Response({'message': "Requested status doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		try:
			group = Group.objects.get(pk=pk)
			serializer = GroupSerializer(group, data=request.data)
			if serializer.is_valid():
				serializer.save()
			else:
				return Response({'errors': serializer.errors, 'message': "Group update failed"}, status=status.HTTP_400_BAD_REQUEST)
			return Response({'data': serializer.data, 'message': "Group updated successfully"}, status=status.HTTP_200_OK)
		except Group.DoesNotExist:
			return Response({'message': "Requested status doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)

	def patch(self, request, pk, format=None):
		try:
			data = request.data
			print('data: ', data)
			group = Group.objects.get(pk=pk)
			serializer = GroupSerializer(group, data=request.data, partial=True)
			if serializer.is_valid():
				serializer.save()
			else:
				return Response({'errors': serializer.errors, 'message': "Group update failed"}, status=status.HTTP_400_BAD_REQUEST)
			return Response({'data': serializer.data, 'message': "Group updated successfully"}, status=status.HTTP_200_OK)
		except Group.DoesNotExist:
			return Response({'message': "Requested status doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)


	def delete(self, request, pk, format=None):
		try:
			group = Group.objects.get(pk=pk)
			group.delete()
			return Response({'message': "Group deleted successfully"}, status=status.HTTP_200_OK)
		except Group.DoesNotExist:
			return Response({'message': "Requested status doesn't exist"}, status=status.HTTP_400_BAD_REQUEST)




class UserListAPIView(APIView):
	permission_classes = [IsAuthenticated]

	def get(self, request, format=None):
		users = User.objects.all()

		serializer = UserSerializer(users, many=True)
		return Response({'data': serializer.data}, status=status.HTTP_200_OK)
