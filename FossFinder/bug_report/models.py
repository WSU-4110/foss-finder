from django.db import models

# Create your models here.
class SubmittedBugs(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField(upload_to="img/")
    