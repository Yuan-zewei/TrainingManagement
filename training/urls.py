from django.urls import path
from . import views
from django.contrib.auth import views as auto_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auto_views.LoginView.as_view(), name='login'),
    path('register/',views.register,name='register'),
]
