from django.urls import path

from user_api.views import UserListView, UserAddressListXMLView

urlpatterns = [
    path('api/users/', UserListView.as_view(), name='json-users'),
    path('rss/users/<int:user_id>/addresses/', UserAddressListXMLView.as_view(), name='rss-user-addresses'),
]
