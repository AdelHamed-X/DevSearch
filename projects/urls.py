from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<str:pk>', views.project, name='project'),
    path('create-project', views.create_project, name='create-project'),
]
