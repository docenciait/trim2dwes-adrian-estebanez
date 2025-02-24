from django.db import models

# Create your models here.
class denuncias(models.Model):
    id = models.IntegerField(unique=True, primary_key= True)  
    Imagen = models.ImageField(upload_to='Images/', blank=True, null=False)  
    User = models.CharField(max_length = 100, unique=True)
    title = models.CharField (max_length=100, blank=False)
    descripcion = models.TextField(max_length=500, blank=False)  
    date = models.DateField(blank=False, null= False)  
    categoria = models.CharField(max_length= 50, blank= False)
    estado = models. CharField(max_length= 100, blank=False)
     


 