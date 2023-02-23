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

    image = models.ImageField(upload_to="img/")
    #image = models.URLField(max_length=200)
    # url feild worked to upload to database
    # while image feild works to view image
    # id 1 has imagefield 2 has urlfield