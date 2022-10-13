from django.urls import path

from user_api.views import UserListJSONView, UserListXMLView

urlpatterns = [
    path('api/users/', UserListJSONView.as_view(), name='json-users'),
    path('rss/users/', UserListXMLView.as_view(), name='rss-users'),
]
