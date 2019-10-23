from django.conf import settings
from django.db import models
from django.utils import timezone


class Free(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    email = models.TextField(blank=True)
    phone  = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def hide(self):
        self.published_date = None
        self.save()
