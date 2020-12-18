from django.contrib import admin
from .models import PaginaInicio, PaginaDonaciones,PaginaContacto, PaginaAdopcion, PaginaBlog, Contact

@admin.register(PaginaInicio)
class PaginaInicioAdmin(admin.ModelAdmin):

    fields = ['head_image', 'description']

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['head_image', 'description', 'seo_description']
        else:
            return self.fields


@admin.register(PaginaContacto)
class PaginaContactoAdmin(admin.ModelAdmin):

    fields = ['head_image',]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['head_image', 'seo_description']
        else:
            return self.fields


@admin.register(PaginaBlog)
class PaginaBlogAdmin(admin.ModelAdmin):

    fields = ['head_image',]

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['head_image', 'seo_description']
        else:
            return self.fields


@admin.register(PaginaAdopcion)
class PaginaAdopcionAdmin(admin.ModelAdmin):

    fields = ['head_image']

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['head_image', 'seo_description']
        else:
            return self.fields


@admin.register(PaginaDonaciones)
class PaginaDonacionesAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            'Página', {
                'fields': ('head_image',)
            }
        ),
        (
            'CBU', {
                'fields': ('info_cbu',)
            }
        ),
        (
            'Mercado Pago', {
                'fields': ('info_mp', 'mp_qr')
            }
        ),
        (
            'PayPal', {
                'fields': ('info_pp', 'pp_qr')
            }
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            fieldsets = (
                (
                    'Página', {
                        'fields': ('head_image', 'seo_description')
                    }
                ),
                (
                    'CBU', {
                        'fields': ('info_cbu',)
                    }
                ),
                (
                    'Mercado Pago', {
                        'fields': ('info_mp', 'mp_qr')
                    }
                ),
                (
                    'PayPal', {
                        'fields': ('info_pp', 'pp_qr')
                    }
                ),
            )
            return fieldsets
        else:
            return self.fieldsets

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('subject', 'contact_category', 'email', 'tel', 'date', 'answered')
    list_filter = ('contact_category', 'date', 'answered')