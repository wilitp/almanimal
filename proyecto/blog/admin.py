from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['created_date', 'last_updated']
    list_display = ['author', 'created_date', 'last_updated']

admin.site.register(Blog)
