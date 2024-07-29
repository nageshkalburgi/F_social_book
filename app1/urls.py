# users/urls.py
from django.urls import path
from .views import home, register, login
from . import views

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('', login, name='login'),
    path('index',views.index, name='index'),
    path('password_reset',views.password_reset,name='password_reset')
]
