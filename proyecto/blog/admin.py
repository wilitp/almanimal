from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['created_date', 'last_updated']
    list_display = ['title', 'author', 'last_updated', 'created_date']
    list_filter = ('author', 'last_updated', 'created_date')
    actions = ['mark_as_published', 'mark_as_not_published']

    def mark_as_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, ngettext(
            '%d blog fué marcado como publicado.',
            '%d blogs fueron marcados como publicados.',
            updated,
        ) % updated, messages.SUCCESS)
    mark_as_published.short_description = "PUBLICADO"

    def mark_as_not_published(self, request, queryset):
        updated = queryset.update(published=False)
        self.message_user(request, ngettext(
            '%d blog fué marcado como no publicado.',
            '%d blogs fueron marcados como no publicados.',
            updated,
        ) % updated, messages.SUCCESS)
    mark_as_not_published.short_description = "NO PUBLICADO"