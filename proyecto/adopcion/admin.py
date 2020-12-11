from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    readonly_fields  = ['actualizado', 'creado', 'image_tag', 'image_tag2']
    list_display = ['nombre', 'tipo_animal', 'raza_perro', 'raza_gato', 'creado', 'publicado', 'image_tag']
    list_filter = ('tipo_animal', 'raza_perro', 'raza_gato', 'creado', 'publicado')
    actions = ['mark_as_published', 'mark_as_not_published']
    fieldsets = (
        (
            'Información del animal', {
                'fields': ('nombre', 'tipo_animal', 'raza_perro', 'raza_gato', 'tamaño', 'foto1', 'image_tag', 'foto2', 'image_tag2', 'edad', 'tiempo', 'sexo', 'descripcion', 'caracter', 'vacunado', 'desparasitado', 'castrado', 'comentario')
            }
        ),
        (
            'Información del creador', {
                'fields': ('dueño', 'telefono', 'email')
            }
        ),
        (
            'Información de la publicación', {
                'fields': ('publicado', 'actualizado', 'creado')
            }
        ),
    )

    def mark_as_published(self, request, queryset):
        updated = queryset.update(publicado=True)
        self.message_user(request, ngettext(
            '%d animal fué marcado como publicado.',
            '%d animales fueron marcados como publicados.',
            updated,
        ) % updated, messages.SUCCESS)
    mark_as_published.short_description = "PUBLICADO"

    def mark_as_not_published(self, request, queryset):
        updated = queryset.update(publicado=False)
        self.message_user(request, ngettext(
            '%d animal fué marcado como no publicado.',
            '%d animales fueron marcados como no publicados.',
            updated,
        ) % updated, messages.SUCCESS)
    mark_as_not_published.short_description = "NO PUBLICADO"