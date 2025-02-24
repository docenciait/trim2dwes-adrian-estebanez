from django.contrib import admin  
from django.urls import path, include  
from . import views  

# Define las rutas de URL para la aplicación
urlpatterns = [
    path('login/', views.user_login, name='login'),  

    path('registro/', views.register, name='registro'),  

    path('registro/', views.clean, name='registro'),  
]