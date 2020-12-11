from django.db import models
from django.forms import ModelForm

from ckeditor.fields import RichTextField

class Contact(models.Model):
    first_name = models.CharField("Nombre", max_length=20)
    last_name = models.CharField("Apellido", max_length=20)
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
        "Categoría",
        max_length=10,
        choices=CONTACT_CATEGORY_CHOICES,
        default='CONSULTA'
    )
    subject = models.CharField("Asunto", max_length=80)
    body = models.CharField("Cuerpo", max_length=2000)
    answered = models.BooleanField("Contestado", default=False)
    date = models.DateTimeField("Fecha", auto_now_add=True)


    def __str__(self):
        return f'{self.subject} - {self.first_name}'

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"


class PaginaInicio(models.Model):

    description = RichTextField(verbose_name="Texto")
    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina inicio'

    class Meta:
        verbose_name_plural = "Página inicio"


class PaginaDonaciones(models.Model):

    info_cbu = RichTextField(verbose_name="Info de CBU", default="Actualmente no disponible.")
    
    seo_description = models.CharField("SEO", max_length=255)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return 'Informacion de la pagina de donaciones'

    class Meta:
        verbose_name_plural = "Página donaciones"


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
