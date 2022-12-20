from django.urls import path
from . import views

urlpatterns = [

    path('Register', views.Register, name='Registers'),
    path('Login', views.Login, name='Logins'),
    path('Logout', views.Logout, name='Logouts'),

]
