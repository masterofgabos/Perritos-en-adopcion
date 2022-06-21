from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'username': 'Usuario',
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'email': 'Email',
        }

class CuentaForm(UserChangeForm):

    class Meta:
        model = User
        fields = [
                'first_name',
                'last_name',
                'email',
            ]
        labels = {
                'first_name': 'Nombre',
                'last_name': 'Apellido',
                'email': 'Email',
        }