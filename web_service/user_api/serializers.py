from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(source='username')

    class Meta:
        model = User
        fields = (
            'identifier',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )
