from django.shortcuts import render, HttpResponse, redirect  # Importa las funciones necesarias para renderizar plantillas, devolver respuestas HTTP y redirigir.
from django.contrib.auth import authenticate, login  # Importa funciones para autenticar y hacer login con un usuario.
from usuarios.forms import LoginForm  # Importa el formulario de login definido en el archivo forms.py.
from usuarios.forms import CreateUserForm  # Importa el formulario para crear usuarios desde forms.py.
from django.utils.crypto import get_random_string  # Importa la función para generar cadenas aleatorias (aunque no se usa en este código).
from django.contrib import messages  # Importa el sistema de mensajes de Django para mostrar mensajes al usuario.
from django.contrib.auth.models import User  # Importa el modelo User de Django para trabajar con usuarios.
from django.core.mail import send_mail  # Importa la función para enviar correos electrónicos (aunque no se usa en este código).
from django.contrib.auth import logout
# Vista para manejar el login de los usuarios.
def user_login(request):
    if request.method == 'POST':  # Si la solicitud es un POST (enviado el formulario).
        form = LoginForm(request.POST)  # Se crea una instancia del formulario de login con los datos enviados.
        if form.is_valid():  # Si el formulario es válido (datos correctos).
            cd = form.cleaned_data  # Obtiene los datos validados del formulario.
            user = authenticate(request, username=cd['username'], password=cd['password'])  # Intenta autenticar al usuario con los datos proporcionados.
            if user is not None:  # Si el usuario existe.
                if user.is_active:  # Si la cuenta está activa.
                    login(request, user)  # Inicia sesión al usuario.
                    return HttpResponse('Autenticación exitosa')  # Devuelve una respuesta indicando que la autenticación fue exitosa.
                else:
                    return HttpResponse('Cuenta desactivada')  # Si la cuenta está desactivada, muestra un mensaje.
            else:
                return HttpResponse('Credenciales inválidas')  # Si las credenciales no son correctas, muestra un mensaje.
    else:
        form = LoginForm()  # Si la solicitud no es POST (es la primera vez que se carga la página), crea un formulario vacío.
    
    return render(request, 'usuarios/login.html', {'form': form})  # Renderiza la plantilla 'login.html' y pasa el formulario al contexto.

# Vista para manejar el registro de usuarios.
def register(request):
    if request.method == 'POST':  
        form = CreateUserForm(request.POST)  # Crea una instancia del formulario de creación de usuario con los datos enviados.
        if form.is_valid():  # Si el formulario es válido.
            user = form.save()  # Guarda el nuevo usuario en la base de datos.
            login(request, user)  # Inicia sesión automáticamente al usuario recién creado.
            return redirect('home')  # Redirige al usuario a la página principal ('home').
    else:
        form = CreateUserForm()  # Si la solicitud no es POST, crea un formulario vacío.
    
    return render(request, 'usuarios/register.html', {'form': form})  # Renderiza la plantilla 'register.html' y pasa el formulario al contexto.

# Vista para manejar el registro de usuarios, aunque es redundante con la vista anterior.
def clean(request):
    if request.method == 'POST':  # Si la solicitud es un POST (formulario enviado).
        form = CreateUserForm(request.POST)  # Crea una instancia del formulario de creación de usuario con los datos enviados.
        if form.is_valid():  # Si el formulario es válido.
            user = form.save()  # Guarda el nuevo usuario en la base de datos.
            login(request, user)  # Inicia sesión automáticamente al usuario recién creado.
            return redirect('home')  # Redirige al usuario a la página principal ('home').
    else:
        form = CreateUserForm()  # Si la solicitud no es POST, crea un formulario vacío.
    
    return render(request, 'usuarios/register.html', {'form': form})  # Renderiza la plantilla 'register.html' y pasa el formulario al contexto.

# Vista para cerrar sesión
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')  # Redirige a la página de login después del logout



