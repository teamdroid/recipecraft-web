import os

from django.db import models
from django.dispatch import receiver


# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to="apps/")
    upload_date = models.DateTimeField(auto_now_add=True)


@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from file system"""
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)
