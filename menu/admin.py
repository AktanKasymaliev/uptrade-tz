from django.contrib import admin

from menu.models import Notes

@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'url')
