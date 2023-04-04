from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from django.contrib.auth.models import User



class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('profile_id', 'profile_image')




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['is_staff', 'is_superuser', 'password', 'user_permissions', 'groups']
        