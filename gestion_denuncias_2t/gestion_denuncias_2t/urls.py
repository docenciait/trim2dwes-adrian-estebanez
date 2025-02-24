"""
URL configuration for gestion_denuncias_2t project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # Importa el módulo de administración de Django para agregar la URL del panel de administración.
from django.urls import path, include  # Importa las funciones path y include para definir rutas y vincular archivos de URL adicionales.
from django.http import HttpResponse  # Importa HttpResponse para devolver respuestas HTTP simples.

# Vista para la URL base
def home(request):
    return HttpResponse("¡Bienvenido a la página principal!")  # Devuelve una respuesta HTTP con un mensaje simple en la página principal.

# Lista de URL y sus vistas correspondientes
urlpatterns = [
    path('', home, name='home'),  
    path('admin/', admin.site.urls),  
    path('denuncias/', include('denuncias.urls')), 
    path('usuarios/', include('usuarios.urls')),
]

