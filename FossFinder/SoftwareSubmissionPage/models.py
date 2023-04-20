from django.db import models

# Create your models here.
class SubmittedSoftware(models.Model):
    name = models.CharField(max_length=25)
    developer = models.CharField(max_length=25)
    description = models.TextField()


    tag_WordProcesser = models.BooleanField(default=False)
    tag_SpreadSheet = models.BooleanField(default=False)
    tag_GraphicsEditor = models.BooleanField(default=False)
    tag_AudioEditor = models.BooleanField(default=False)
    tag_Communication = models.BooleanField(default=False)
    tag_Multimedia = models.BooleanField(default=False)
    tag_AntiVirus = models.BooleanField(default=False)
    tag_CodeEditor = models.BooleanField(default=False)
    tag_DiskBurner = models.BooleanField(default=False)
    tag_FileShare = models.BooleanField(default=False)
    tag_Other = models.BooleanField(default=False)


    os_WIN = models.BooleanField(default=False)
    os_MAC = models.BooleanField(default=False)
    os_NIX = models.BooleanField(default=False)


    image = models.URLField(max_length=200)