from django.forms import ModelForm
from django import forms
from .models import Animal

TIPO_ANIMAL = (
    ('Perro', 'Perro'),
    ('Gato', 'Gato'),
    ('Otro', 'Otro'),
)

TAMAÑO = (
    ('Chico', 'Chico'),
    ('Mediano', 'Mediano'),
    ('Grande', 'Grande'),
)

SEXO = (
    ('Macho', 'Macho'),
    ('Hembra', 'Hembra'),
    ('Indefinido', 'Indefinido'),
)

TIEMPO = (
    ('Dias', 'Días'),
    ('Semanas', 'Semanas'),
    ('Meses', 'Meses'),
    ('Años', 'Años'),
)

RAZA_GATO = (
    ('Mestizo', 'Mestizo'),
    ('Americano De Pelo Corto', 'Americano De Pelo Corto'),
    ('Angora Turco', 'Angora Turco'),
    ('Azul Ruso', 'Azul Ruso'),
    ('Bengali', 'Bengali'),
    ('Bombay', 'Bombay'),
    ('British Shorthair', 'British Shorthair'),
    ('Europeo De Pelo Corto', 'Europeo De Pelo Corto'),
    ('Persa', 'Persa'),
    ('Sagrado De Birmania', 'Sagrado De Birmania'),
    ('Siames', 'Siames'),
    ('Snowshoe', 'Snowshoe'),
)

RAZA_PERRO = (
    ('Mestizo', 'Mestizo'),
    ('Akita Inu', 'Akita Inu'),
    ('Basset Hound O Batata', 'Basset Hound O Batata'),
    ('Beagle', 'Beagle'),
    ('Bichon Frise', 'Bichon Frise'),
    ('Border Collie', 'Border Collie'),
    ('Boxer', 'Boxer'),
    ('Braco Aleman Kurzhaar', 'Braco Aleman Kurzhaar'),
    ('Braco hungaro O Vizsla', 'Braco hungaro O Vizsla'),
    ('Breton', 'Breton'),
    ('Bull Terrier', 'Bull Terrier'),
    ('Bulldog Frances', 'Bulldog Frances'),
    ('Bulldog Ingles', 'Bulldog Ingles'),
    ('Caniche', 'Caniche'),
    ('Chihuahua', 'Chihuahua'),
    ('Chow Chow', 'Chow Chow'),
    ('Cocker Spaniel', 'Cocker Spaniel'),
    ('Collie', 'Collie'),
    ('Dachshund O Salchicha', 'Dachshund O Salchicha'),
    ('Dalmata', 'Dalmata'),
    ('Doberman', 'Doberman'),
    ('Dogo Argentino', 'Dogo Argentino'),
    ('Dogo de Burdeos', 'Dogo de Burdeos'),
    ('Fox Terrier', 'Fox Terrier'),
    ('Galgo', 'Galgo'),
    ('Golden Retriever', 'Golden Retriever'),
    ('Gran Danes', 'Gran Danes'),
    ('Jack Russell Terrier', 'Jack Russell Terrier'),
    ('Labrador Retriever', 'Labrador Retriever'),
    ('Lhasa Apso', 'Lhasa Apso'),
    ('Maltes', 'Maltes'),
    ('Mastin Napolitano', 'Mastin Napolitano'),
    ('Ovejero Aleman', 'Ovejero Aleman'),
    ('Pastor Belga', 'Pastor Belga'),
    ('Pastor Ingles', 'Pastor Ingles'),
    ('Pekines', 'Pekines'),
    ('Pila', 'Pila'),
    ('Pinscher', 'Pinscher'),
    ('Pitbull', 'Pitbull'),
    ('Pointer', 'Pointer'),
    ('Presa Canario', 'Presa Canario'),
    ('Pug', 'Pug'),
    ('Rottweiler', 'Rottweiler'),
    ('Samoyedo', 'Samoyedo'),
    ('San Bernardo', 'San Bernardo'),
    ('Schnauzer', 'Schnauzer'),
    ('Setter Irlandes', 'Setter Irlandes'),
    ('Shar Pei', 'Shar Pei'),
    ('Shiba Inu', 'Shiba Inu'),
    ('Shih TzuHusky Siberiano', 'Shih TzuHusky Siberiano'),
    ('Weimaraner', 'Weimaraner'),
    ('Whippet', 'Whippet'),
    ('Yorkshire Terrier', 'Yorkshire Terrier'),
)

class AnimalForm(ModelForm):

    nombre = forms.CharField(label="Nombre", max_length=30, required=True, widget=forms.TextInput(
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

    raza_perro = forms.ChoiceField(label="Raza", choices=RAZA_PERRO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    raza_gato = forms.ChoiceField(label="Raza", choices=RAZA_GATO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    tamaño = forms.ChoiceField(label="Tamaño", choices=TAMAÑO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
        }
    ))

    edad = forms.CharField(label="Edad", max_length=2, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Edad*',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'tel'
        }
    ))

    tiempo = forms.ChoiceField(label="Tiempo", choices=TIEMPO, required=True, widget=forms.Select(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;'
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
            'placeholder' : 'Descripcion... (*)'
        }
    ))

    caracter = forms.CharField(label="Carácter", required=True, widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'placeholder' : 'Caracter... (*)'
        }
    ))

    comentario = forms.CharField(label="Comentario", required=False, widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'placeholder' : 'Comentario... (opcional)'
        }
    ))

    telefono = forms.CharField(label="Teléfono de contacto", max_length=20, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Teléfono*',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'tel'
        }
    ))

    email = forms.CharField(label="Email de contacto", max_length=50, required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Email*',
            'style' : 'margin-bottom:20px; margin-top:20px;',
            'type' : 'email'
        }
    ))

    class Meta:
        model = Animal
        fields = (
            'nombre',
            'tipo_animal',
            'raza_perro',
            'raza_gato',
            'tamaño',
            'foto1',
            'foto2',
            'edad',
            'tiempo',
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