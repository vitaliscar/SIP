
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class ThemePreferenceForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['theme_preference']
        widgets = {
            'theme_preference': forms.RadioSelect(choices=CustomUser.THEME_CHOICES)
        }
        labels = {
            'theme_preference': 'Modo de visualización'
        }

# Formulario de registro para CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'codigo_asesor',
            'sucursal',
            'rol',
            'first_name',
            'last_name',
            'theme_preference',
        ]
        labels = {
            'username': 'Usuario',
            'email': 'Correo electrónico',
            'codigo_asesor': 'Código Asesor',
            'sucursal': 'Sucursal',
            'rol': 'Rol',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'theme_preference': 'Preferencia de tema',
        }
