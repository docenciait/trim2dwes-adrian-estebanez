from django.contrib import admin

# Register your models here.

from .models import denuncias  # Importa el modelo 'Account' desde el archivo 'models.py' en la misma aplicación.

admin.site.register(denuncias)