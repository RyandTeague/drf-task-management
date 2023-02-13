from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

	class Meta:
		model = Todo
		fields = ('id', 'title', 'description', 'completed',
            'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            )