from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.loginPage, name="loginPage"),
    path('auth/register', views.registerPage, name="registerPage"),
    path('logout', views.logout, name="logout")
]
