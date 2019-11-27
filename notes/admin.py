from django.contrib import admin

from notes.models import Note, Topic


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'description', 'created', 'modified')
    pass


admin.site.register(Note, NoteAdmin)
admin.site.register(Topic, TopicAdmin)
