from django.urls import path
from .views import get_user, user_details
from .views import create_user

urlpatterns = [
    path('users/', get_user, name='get_user'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_details, name='user_details')
]