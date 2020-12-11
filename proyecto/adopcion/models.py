from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.templatetags.static import static
from core.image_compress import compress

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

    class RazaGato(models.TextChoices):
        MESTIZO = 'Mestizo'
        AMERICANO_DE_PELO_CORTO = 'Americano De Pelo Corto'
        ANGORA_TURCO = 'Angora Turco'
        AZUL_RUSO = 'Azul Ruso'
        BENGALI = 'Bengali'
        BOMBAY = 'Bombay'
        BRITISH_SHORTHAIR = 'British Shorthair'
        EUROPEO_DE_PELO_CORTO = 'Europeo De Pelo Corto'
        PERSA = 'Persa'
        SAGRADO_DE_BIRMANIA = 'Sagrado De Birmania'
        SIAMES = 'Siames'
        SNOWSHOE = 'Snowshoe'

    class RazaPerro(models.TextChoices):
        MESTIZO = 'Mestizo'
        AKITA_INU = 'Akita Inu'
        BASSET_HOUND_O_BATATA = 'Basset Hound O Batata'
        BEAGLE = 'Beagle'
        BICHON_FRISE = 'Bichon Frise'
        BORDER_COLLIE = 'Border Collie'
        BOXER = 'Boxer'
        BRACO_ALEMAN_KURZHAAR = 'Braco Aleman Kurzhaar'
        BRACO_HUNGARO_O_VIZSLA = 'Braco hungaro O Vizsla'
        BRETON = 'Breton'
        BULL_TERRIER = 'Bull Terrier'
        BULLDOG_FRANCES = 'Bulldog Frances'
        BULLDOG_INGLES = 'Bulldog Ingles'
        CANICHE = 'Caniche'
        CHIHUAHUA = 'Chihuahua'
        CHOW_CHOW = 'Chow Chow'
        COCKER_SPANIEL = 'Cocker Spaniel'
        COLLIE = 'Collie'
        DACHSHUND_O_SALCHICHA = 'Dachshund O Salchicha'
        DALMATA = 'Dalmata'
        DOBERMAN = 'Doberman'
        DOGO_ARGENTINO = 'Dogo Argentino'
        DOGO_DE_BURDEOS = 'Dogo de Burdeos'
        FOX_TERRIER = 'Fox Terrier'
        GALGO = 'Galgo'
        GOLDEN_RETRIEVER = 'Golden Retriever'
        GRAN_DANES = 'Gran Danes'
        JACK_RUSSELL_TERRIER = 'Jack Russell Terrier'
        LABRADOR_RETRIEVER = 'Labrador Retriever'
        LHASA_APSO = 'Lhasa Apso'
        MALTES = 'Maltes'
        MASTIN_NAPOLITANO = 'Mastin Napolitano'
        OVEJERO_ALEMAN = 'Ovejero Aleman'
        PASTOR_BELGA = 'Pastor Belga'
        PASTOR_INGLES = 'Pastor Ingles'
        PEKINES = 'Pekines'
        PILA = 'Pila'
        PINSCHER = 'Pinscher'
        PITBULL = 'Pitbull'
        POINTER = 'Pointer'
        PRESA_CANARIO = 'Presa Canario'
        PUG = 'Pug'
        ROTTWEILER = 'Rottweiler'
        SAMOYEDO = 'Samoyedo'
        SAN_BERNARDO = 'San Bernardo'
        SCHNAUZER = 'Schnauzer'
        SETTER_IRLANDES = 'Setter Irlandes'
        SHAR_PEI = 'Shar Pei'
        SHIBA_INU = 'Shiba Inu'
        SHIH_TZUHUSKY_SIBERIANO = 'Shih TzuHusky Siberiano'
        WEIMARANER = 'Weimaraner'
        WHIPPET = 'Whippet'
        YORKSHIRE_TERRIER = 'Yorkshire Terrier'


    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animales'


    def __str__(self):
        return self.nombre

    dueño = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Creador', limit_choices_to={'is_staff':True})
    nombre = models.CharField(verbose_name='Nombre', max_length=30, null=False, blank=False)
    tipo_animal = models.CharField(verbose_name='Tipo de animal', max_length=40, choices=TipoAnimal.choices, null=False, blank=False)
    raza_perro = models.CharField(verbose_name='Raza Perro', help_text='Dejar en blanco si es Gato u Otro', max_length=255, choices=RazaPerro.choices, null=True, blank=True)
    raza_gato = models.CharField(verbose_name='Raza Gato', help_text='Dejar en blanco si es Perro u Otro', max_length=255, choices=RazaGato.choices, null=True, blank=True)
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

        # Comprimiendo imagenes
        if self.foto1:
            if self.foto1.size > 1000000:
                self.foto1 = compress(self.foto1)
        
        if self.foto2:
            if self.foto2.size > 1000000:
                self.foto2 = compress(self.foto2)

        # Chequeando el tipo de animal para dejar en nulo los camplos innecesarios
        if str(self.tipo_animal) == 'Perro':
            self.raza_gato = None
        elif str(self.tipo_animal) == 'Gato':
            self.raza_perro = None
        else:
            self.raza_perro = None
            self.raza_gato = None


        super(Animal, self).save(*args, **kwargs)

