from django.urls import path

from user_api.views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='home'),
]
