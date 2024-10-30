from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListAPI.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
]