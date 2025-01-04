from django.urls import path
from . import views


app_name= 'account'

urlpatterns=[
    path('list', views.user_list, name='user_list'),
    path('login', views.user_login, name='user_login'),
    path('logout', views.user_logout, name='user_logout'),
    path('register', views.user_register, name='user_register'),
]