from django.db import models
from django.forms import ModelForm

from ckeditor.fields import RichTextField

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
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
    answered = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.subject} - {self.first_name}'


class PaginaInicio(models.Model):

    description = RichTextField(verbose_name="Texto")
    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina inicio'


class PaginaDonaciones(models.Model):

    description = RichTextField(verbose_name="Texto")
    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina de donaciones'


class PaginaContacto(models.Model):

    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina Contacto'


class PaginaBlog(models.Model):

    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina Blog'


class PaginaAdopcion(models.Model):

    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina Adopcion'