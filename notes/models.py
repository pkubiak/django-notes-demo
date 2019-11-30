import time
from django.db import models
from django.conf import settings
from django.urls import reverse
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from mptt.models import MPTTModel, TreeForeignKey


class Topic(TitleSlugDescriptionModel, TimeStampedModel, MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['slug']

    def __str__(self):
        return self.title


class Note(TimeStampedModel, models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    topic = TreeForeignKey(Topic, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})

    @property
    def topics(self):
        return self.topic.get_ancestors(ascending=False, include_self=True)
