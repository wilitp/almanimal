from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):

    username = forms.CharField(label="", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        }
    ))

    email = forms.EmailField(label="", required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'type': 'email'
        }
    ))

    password1 = forms.CharField(label="", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Contraseña'
        }
    ))

    password2 = forms.CharField(label="", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'password',
            'placeholder': 'Repita contraseña'
        }
    ))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )