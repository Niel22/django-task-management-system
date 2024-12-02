from django.urls import path
from . import views

urlpatterns = [
    path('auth/login', views.loginPage, name="login"),
    path('auth/register', views.registerPage, name="register")
]
