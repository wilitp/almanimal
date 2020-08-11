from django.contrib import admin

from .models import Animal


# Register your models here.


class AnimalAdmin(admin.ModelAdmin):

    readonly_fields  = ['actualizado', 'creado']
    list_display = ['nombre', 'tipo_animal', 'raza']

admin.site.register(Animal, AnimalAdmin)