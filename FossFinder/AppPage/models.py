from django.db import models

# Create your models here.
class Software(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()
    developer = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    download_link = models.URLField()