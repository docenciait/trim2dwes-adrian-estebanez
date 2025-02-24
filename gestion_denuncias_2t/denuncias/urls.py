from django.contrib import admin  
from django.urls import path, include  
from . import views  


urlpatterns = [
    path('crear_denuncias/', views.CrearDenuncias, name='CrearDenuncias'),  
 

    path('crear_denuncias/', views.clean, name='CrearDenuncias'),
    
    path('lista_denuncias/', views.listar_denuncias, name='ListarDenuncias'),  
]