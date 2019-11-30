from django.contrib import admin

from notes.models import Note, Topic
from django_mptt_admin.admin import DjangoMpttAdmin


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'modified')


class TopicAdmin(DjangoMpttAdmin):
    list_display = ('slug', 'title', 'description', 'created', 'modified')



admin.site.register(Note, NoteAdmin)
admin.site.register(Topic, TopicAdmin)
