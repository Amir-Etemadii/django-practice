from django.urls import path
from . import  views

app_name= 'courses'

urlpatterns=[
    path('list', views.course_list, name='list'),
    path('detail/<int:course_id>', views.course_details, name='details'),
    path('add', views.course_add, name='add'),
]