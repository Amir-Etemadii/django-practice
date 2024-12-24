from django.urls import path
from . import views

home_app= 'home'

urlpatterns= [
    path('', views.index, name='index'),
]