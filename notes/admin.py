from django.contrib import admin

from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')


admin.site.register(Note, NoteAdmin)
