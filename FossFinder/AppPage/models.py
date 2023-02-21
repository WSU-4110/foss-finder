from django.db import models

# Create your models here.
class Software(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.FilePathField(path="/img")