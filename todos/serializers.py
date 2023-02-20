from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    friends = serializers.StringRelatedField(many=True)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Todo
        fields = ['id', 'owner', 'is_owner', 'friends', 'title', 'description', 'deadline', 'completed', 'created', 'updated_at']
        read_only_fields = ['id', 'created', 'updated_at']
