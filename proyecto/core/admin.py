from django.contrib import admin
from .models import PaginaInicio, PaginaDonaciones,PaginaContacto, PaginaAdopcion, PaginaBlog, Contact

admin.site.register(Contact)
admin.site.register(PaginaInicio)
admin.site.register(PaginaDonaciones)
admin.site.register(PaginaContacto)
admin.site.register(PaginaBlog)
admin.site.register(PaginaAdopcion)
