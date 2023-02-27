from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Group
        fields = ['id', 'owner', 'name', 'members', 'created_at']
        read_only_fields = ['id', 'created_at']
