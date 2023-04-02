from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group

from drf_tsk.serializers import UserSerializer




class GroupListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    members = UserSerializer(many=True)

    def get_is_owner(self, obj):
        request = self.context.get('request')
        return request.user == obj.owner

    class Meta:
        model = Group
        fields = ['id', 'owner', 'is_owner', 'name', 'members', 'created_at']
        read_only_fields = ['id', 'created_at']



class GroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ['id', 'owner', 'name', 'members', 'created_at']
        read_only_fields = ['id', 'created_at']
