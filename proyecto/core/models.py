from django.db import models
from django.db import signals
from django.forms import ModelForm


class Contact(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    tel = models.CharField(max_length=15)
    CONTACT_CATEGORY_CHOICES = [
    ('CONSULTA', 'Consulta'),
    ('SUGERENCIA', 'Sugerencia'),
    ('URGENTE', 'Urgente'),
    ('DONACIONES', 'Donaciones'),
    ('OFERTA', 'Oferta'),
    ('OTRO', 'Otro'),
    ]
    contact_category = models.CharField(
        max_length=10,
        choices=CONTACT_CATEGORY_CHOICES,
        default='CONSULTA'
    )
    subject = models.CharField(max_length=80)
    body = models.CharField(max_length=2000)
    answered = models.BooleanField()


    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'tel', 'contact_category', 'subject', 'body']
