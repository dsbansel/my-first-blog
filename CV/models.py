from django.db import models
from django.conf import settings
from django.utils import timezone

class Section(models.Model):
    header = models.CharField(max_length=200)
    text = models.TextField()
    last_edited = models.DateTimeField(blank=True, null=True)

    def update(self):
        self.last_edited = timezone.now()
        self.save()

    def __str__(self):
        return self.header