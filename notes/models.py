import time
from django.db import models
from django.conf import settings
from django.urls import reverse


class Note(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    published_at = models.DateTimeField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def get_absolute_url(self):
        return reverse('note-detail', kwargs={'pk': self.pk})
