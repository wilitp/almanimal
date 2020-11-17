from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['created_date', 'last_updated']
    list_display = ['title', 'author', 'last_updated', 'created_date']
    list_filter = ('author', 'last_updated', 'created_date')
