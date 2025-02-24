from django.shortcuts import render
from pyexpat.errors import messages
from django.shortcuts import redirect, get_object_or_404
from .models import denuncias 
from django.urls import reverse

def CrearDenuncias(request):
    if request.method == 'POST':  
        form = CrearDenunciasForm(request.POST)  
        if form.is_valid():  
            id = form.save()  
            return redirect('home')  
    else:
        form = CrearDenunciasForm()  
    
    return render(request, 'denuncias/crear_denuncias.html', {'form': form})  


def clean(request):
    if request.method == 'POST':  
        form = CrearDenunciasForm(request.POST)  
        if form.is_valid():  
            id = form.save()   
            return redirect('home') 
    else:
        form = CreateUserForm()  
    
    return render(request, 'denuncias/crear_denuncias.html', {'form': form})  

denuncias = []
def listar_denuncias(request):
    denuncias = denuncias.object.all()
    return render (request, 'lista_denuncias.html',{'denuncias': denuncias })