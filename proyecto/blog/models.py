from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from core.image_compress import compress


class Blog(models.Model):

    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE, limit_choices_to={'is_staff':True})
    title = models.CharField("Título", max_length=50, default="")
    photo = models.ImageField("Foto de encabezado", upload_to="blog_photo", blank=False, null=False, default="")
    blog_body = RichTextField(verbose_name="Texto")
    published = models.BooleanField("Publicado", default=True)
    created_date = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_updated = models.DateTimeField("Última actualización", auto_now=True)
    photo1 = models.ImageField("Foto 1 (opcional)", upload_to="blog_photo", blank=True, null=True)
    photo2 = models.ImageField("Foto 2 (opcional)", upload_to="blog_photo", blank=True, null=True)

    def __str__(self):
        return f"{self.id}/{self.title}"

    def save(self, *args, **kwargs):
        # Borrando imagenes anteriores cuando son actualizadas
        try:
            this = Blog.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete()
            if this.photo1 != self.photo1:
                this.photo1.delete()
            if this.photo2 != self.photo2:
                this.photo2.delete()
        except:
            pass

        # Comprimiendo imagenes
        if self.photo.size > 1000000:
            self.photo = compress(photo)
        if self.photo1:
            if self.photo1.size > 1000000:
                self.photo1 = compress(photo1)
        if self.photo2:
            if self.photo2.size > 1000000:
                self.photo2 = compress(photo2)
        
        super(Blog, self).save(*args, **kwargs)
    

