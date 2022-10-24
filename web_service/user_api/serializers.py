from django.contrib.auth.models import User

from rest_framework import serializers

from user_api.models import Address

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
        )


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = (
            'id',
            'address',
        )
