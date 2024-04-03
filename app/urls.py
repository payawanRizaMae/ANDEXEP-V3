from django.urls import path
from .views import *

urlpatterns = [
    path('', home_user, name='home_user'),
    path('show-record', show_record, name='show_record'),
    path('login', login_user, name='login_user'),
    path('register', register_user, name='register_user'),
    path('logout', logout_user, name='logout_user'),
    path('delete-record/<int:pk>/', delete_record, name="delete_record"),
    ]
