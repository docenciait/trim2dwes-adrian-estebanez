from django import forms  # Importa el módulo de formularios de Django, que se usa para crear formularios en la web.
from django.contrib.auth.models import User  # Importa el modelo 'User' de Django, que representa a los usuarios en el sistema.


class LoginForm(forms.Form):
    username = forms.CharField()  
    password = forms.CharField(widget=forms.PasswordInput)  

class CreateUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    confirm_password = forms.CharField(widget=forms.PasswordInput)  
    class Meta:  
        model = User  
        fields = ['username', 'first_name', 'email', 'password']  

    
    def clean(self):  
        cleaned_data = self.cleaned_data 
        password = cleaned_data.get('password')  
        confirm_password = cleaned_data.get('confirm_password')  

        
        if password and confirm_password and password != confirm_password:  
            self.add_error('confirm_password', 'Las contraseñas no coinciden.')  n.

        return cleaned_data  # Devuelve los datos limpios (y con posibles errores añadidos).
