from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# app_name = 'auth'
urlpatterns = [
    path("mylogin", views.login, name="login")
    ]