from django.db import models
from ckeditor.fields import RichTextField

class ContenidoHome(models.Model):
  contenido = RichTextField(verbose_name="Texto")
