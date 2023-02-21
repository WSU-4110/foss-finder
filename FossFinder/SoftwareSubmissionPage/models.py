from django.db import models

# Create your models here.
class SubmittedSoftware(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    #tags = models.TextChoices():
        #('Operating System', 'Operating System'),
        #('Office Suite', 'Office Suite'),
        #('Web Browser', 'Web Browser'),
        #('Graphics Editor', 'Graphics Editor'),
        #('Programming Language', 'Programming Language'),)
    similar = models.CharField(max_length=25)
    os = models.CharField(max_length=25)
    image = models.FilePathField(path="/img")