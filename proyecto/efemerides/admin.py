from django.contrib import admin
from .models import Efemerides

@admin.register(Efemerides)
class EfemeridesAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'fecha_festividad')
    list_filter = ('titulo',)
