from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import generics
from rest_framework_xml.parsers import XMLParser

from user_api.models import Address
from user_api.serializers import (
    UserSerializer,
    AddressSerializer
)
from user_api.renderers import AddressXMLRenderer


class UserListView(generics.ListAPIView):
    """
    API endpoint to get list of users in JSON representation.
    """
    queryset = User.objects.all().exclude(username='admin').order_by('-date_joined')
    serializer_class = UserSerializer


class UserAddressListXMLView(generics.ListAPIView):
    """
    API endpoint to get list of addresses belongs to a specific user in XML representation.
    """
    parser_classes = (XMLParser,)
    renderer_classes = (AddressXMLRenderer,)
    serializer_class = AddressSerializer

    def get_queryset(self):
        try:
            user = User.objects.all().exclude(username='admin').get(id=self.kwargs['user_id'])
        except User.DoesNotExist:
            raise Http404

        return Address.objects.filter(user=user)
