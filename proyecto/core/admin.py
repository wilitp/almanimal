from django.contrib import admin
from .models import PaginaInicio, PaginaDonaciones,PaginaContacto, PaginaAdopcion, PaginaBlog, Contact

admin.site.register(PaginaContacto)
admin.site.register(PaginaBlog)
admin.site.register(PaginaAdopcion)

@admin.register(PaginaInicio)
class PaginaInicioAdmin(admin.ModelAdmin):

    fields = ['description',]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['description', 'seo_description']
        else:
            return self.fields


@admin.register(PaginaDonaciones)
class PaginaDonacionesAdmin(admin.ModelAdmin):

    fields = ['description',]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['description', 'seo_description']
        else:
            return self.fields


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('subject', 'contact_category', 'email', 'tel', 'date', 'answered')
    list_filter = ('contact_category', 'date', 'answered')