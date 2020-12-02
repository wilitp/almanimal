from django.contrib import admin

from .models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):

    readonly_fields  = ['dueño', 'actualizado', 'creado', 'image_tag', 'image_tag2']
    list_display = ['nombre', 'tipo_animal', 'raza', 'creado', 'publicado', 'image_tag']
    list_filter = ('tipo_animal', 'raza', 'creado', 'publicado')
    actions = ['mark_as_published', 'mark_as_not_published']
    fieldsets = (
        (
            'Información del animal', {
                'fields': ('nombre', 'tipo_animal', 'raza', 'tamaño', 'foto1', 'image_tag', 'foto2', 'image_tag2', 'edad', 'tiempo', 'sexo', 'descripcion', 'caracter', 'vacunado', 'desparasitado', 'castrado', 'comentario')
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
        queryset.update(publicado=True)
    mark_as_published.short_description = "PUBLICADO"

    def mark_as_not_published(self, request, queryset):
        queryset.update(publicado=False)
    mark_as_not_published.short_description = "NO PUBLICADO"

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['actualizado', 'creado', 'image_tag', 'image_tag2']
        else:
            return self.readonly_fields