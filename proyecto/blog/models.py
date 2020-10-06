from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Blog(models.Model):

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    title = models.CharField("Título", max_length=50, default="")
    photo = models.ImageField("Foto de encabezado", upload_to="blog_photo", blank=False, null=False, default="")
    blog_body = RichTextField(verbose_name="Texto")
    published = models.BooleanField("Publicado", default=True)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)

    def __str__(self):
        return str(self.title) + " - " + str(self.author)
    

