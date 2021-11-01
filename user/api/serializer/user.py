from rest_framework import serializers
from user.models import User

__all__ = [
    'UserSerializer'
]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)
        read_only_fields = ('username', )
