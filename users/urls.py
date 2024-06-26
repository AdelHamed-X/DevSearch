from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),

    path('', views.profiles, name='profiles'),
    path('profile/<str:pk>', views.profile, name='user-profile'),
]
