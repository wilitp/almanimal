from django.forms import ModelForm
from django import forms
from .models import Animal

TIPO_ANIMAL = (
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
)

TAMAÑO = (
    ('Grande', 'Grande'),
    ('Mediano', 'Mediano'),
    ('Chico', 'Chico'),
)

SEXO = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
    ('Indefinido', 'Indefinido'),
)

class AnimalForm(ModelForm):

    nombre = forms.CharField(label="Nombre", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Nombre',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    tipo_animal = forms.ChoiceField(label="Tipo de animal", choices=TIPO_ANIMAL, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    raza = forms.CharField(label="Raza", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Raza',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    tamaño = forms.ChoiceField(label="Tamaño", choices=TAMAÑO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    edad = forms.CharField(label="Edad", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Edad',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'tel'
        }
    ))

    sexo = forms.ChoiceField(label="Sexo", choices=SEXO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    descripcion = forms.CharField(label="Descripción", required=True, widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'placeholder' : 'Descripcion...'
        }
    ))

    caracter = forms.CharField(label="Carácter", required=True, widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'placeholder' : 'Caracter...'
        }
    ))

    comentario = forms.CharField(label="Comentario", required=True, widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'placeholder' : 'Comentario...'
        }
    ))

    telefono = forms.CharField(label="Teléfono de contacto", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Teléfono',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'tel'
        }
    ))

    email = forms.CharField(label="Email de contacto", max_length=255, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'email'
        }
    ))

    class Meta:
        model = Animal
        fields = (
            'nombre',
            'tipo_animal',
            'raza',
            'tamaño',
            'foto1',
            'foto2',
            'edad',
            'sexo',
            'descripcion',
            'caracter',
            'vacunado',
            'desparasitado',
            'castrado',
            'comentario',
            'telefono',
            'email'
        )