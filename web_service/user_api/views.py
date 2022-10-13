from django.contrib.auth.models import User
from rest_framework import generics

from user_api.serializers import UserSerializer


class UserListView(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().exclude(username='admin').order_by('-date_joined')
    serializer_class = UserSerializer
