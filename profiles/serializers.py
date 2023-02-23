from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friends = serializers.StringRelatedField(many=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'is_owner', 'friends', 'first_name', 'email' 'last_name', 'created_at', 'updated_at', 'name', 'bio', 'image']
        read_only_fields = ['id', 'created_at', 'updated_at']
