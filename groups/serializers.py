from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Group
        fields = ['id', 'owner', 'is_owner', 'name', 'members', 'created_at']
        read_only_fields = ['id', 'created_at']
