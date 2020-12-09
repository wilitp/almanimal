from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.templatetags.static import static

# Create your models here.


class Animal(models.Model):

    class Sexo(models.TextChoices):
        MACHO = 'Macho'
        HEMBRA = 'Hembra'
        INDEFINIDO = 'Indefinido'


    class Tamaño(models.TextChoices):
        CHICO = 'Chico'      
        MEDIANO = 'Mediano'
        GRANDE = 'Grande'

    class TipoAnimal(models.TextChoices):
        PERRO = 'Perro'
        GATO = 'Gato'
        OTRO = 'Otro'

    class Tiempo(models.TextChoices):
        DIAS = 'Dias'
        SEMANAS = 'Semanas'
        MESES = 'Meses'
        AÑOS = 'Años'


    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'


    def __str__(self):
        return self.nombre

    dueño = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creador', limit_choices_to={'is_staff':True})
    nombre = models.CharField(verbose_name='Nombre', max_length=30, null=False, blank=False)
    tipo_animal = models.CharField(verbose_name='Tipo de animal', max_length=40, choices=TipoAnimal.choices, null=False, blank=False)
    raza = models.CharField(verbose_name='Raza', max_length=30, null=False, blank=False)
    tamaño = models.CharField(verbose_name='Tamaño', max_length=40, choices=Tamaño.choices, null=False, blank=False)
    foto1 = models.ImageField(verbose_name="Foto 1", blank=True, null=True, upload_to='foto1')
    foto2 = models.ImageField(verbose_name="Foto 2", blank=True, null=True, upload_to='foto2')
    edad = models.IntegerField(verbose_name='Edad', null=False, blank=False)
    tiempo = models.CharField("Tiempo", max_length=20, choices=Tiempo.choices, null=False, blank=False)
    sexo = models.CharField(verbose_name='Sexo', max_length=20, choices=Sexo.choices, null=False, blank=False)
    descripcion = models.TextField(verbose_name='Descripcion', null=False, blank=False)
    caracter = models.TextField(verbose_name='Carácter', null=True, blank=True)
    vacunado = models.BooleanField(verbose_name='Vacunado', null=False, blank=False)
    desparasitado = models.BooleanField(verbose_name='Desparasitado', null=False, blank=False)
    castrado = models.BooleanField(verbose_name='Castrado', null=False, blank=False)
    comentario = models.TextField(verbose_name='Comentarios', null=True, blank=True)
    telefono = models.CharField("Teléfono de contacto", max_length=20)
    email = models.EmailField("Email de contacto", max_length=50)
    publicado = models.BooleanField(verbose_name='Publicado', default=False)
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    actualizado = models.DateTimeField(auto_now=True,verbose_name='Ultima actualización')

    
    def image_tag(self):
        if self.foto1 and hasattr(self.foto1, 'url'):
            return mark_safe(f'<img style="object-fit:cover; height:100px; width:100px" src={self.foto1.url} />')
        else:
            return mark_safe(f'<img style="object-fit:cover; height:100px; width:100px" src={static("/adopcion/img/no-image.png")} />')
    
    image_tag.short_description = ''


    def image_tag2(self):
        if self.foto2 and hasattr(self.foto2, 'url'):
            return mark_safe(f'<img style="object-fit:cover; height:100px; width:100px" src={self.foto2.url} />')
        else:
            return mark_safe(f'<img style="object-fit:cover; height:100px; width:100px" src={static("/adopcion/img/no-image.png")} />')
    
    image_tag2.short_description = ''


    def save(self, *args, **kwargs):
        # Borrando imagen anterior cuando es actualizada
        try:
            this = Animal.objects.get(id=self.id)
            if this.foto1 != self.foto1:
                this.foto1.delete()
            if this.foto2 != self.foto2:
                this.foto2.delete()
        except:
            pass

        # Chequeando si el usuario es staff para determinar si publicado debe ser True o False
        if self.dueño.is_staff:
            self.publicado = True

        super(Animal, self).save(*args, **kwargs)

