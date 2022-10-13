from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework_xml.parsers import XMLParser

from user_api.serializers import UserSerializer
from user_api.renderers import UserXMLRenderer


class BaseUserListView(generics.ListAPIView):
    """
    Base class for retrieving `User` objects.
    """
    queryset = User.objects.all().exclude(username='admin').order_by('-date_joined')
    serializer_class = UserSerializer


class UserListJSONView(BaseUserListView):
    """
    API endpoint to get list of users in JSON representation.
    """
    pass


class UserListXMLView(BaseUserListView):
    """
    API endpoint to get list of users in XML representation.
    """
    parser_classes = (XMLParser,)
    renderer_classes = (UserXMLRenderer,)
