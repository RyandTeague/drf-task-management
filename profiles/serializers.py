from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner','first_name', 'last_name', 'created_at', 'updated_at', 'name',
            'bio', 'image', 'is_owner', 'following_id',
            'posts_count', 'followers_count', 'following_count',
        ]