from django import forms  # Importa el módulo de formularios de Django, que se usa para crear formularios en la web.
from django.contrib.auth.models import User

class CrearDenunciasForm(forms.Form):
    id= forms.IntegerField()
    Imagen = forms.ImageField()  
    User = forms.CharField()
    title = forms.CharField ()
    descripcion = forms.TextField()  
    date = forms.DateField()  
    categoria = forms.CharField()
    estado = forms.CharField()
