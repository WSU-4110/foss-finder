from django.db import models
from strategy_field import StrategyField
from strategy_field.registry import Registry
# Create your models here.

class AbstractSoftwareForm(object):
    def __init__(self, context):
        self.context = context
    def softwareForm(self):
        raise NotImplementedError
    
class win(AbstractSoftwareForm):
    def softwareForm(self):
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
        image = models.ImageField(upload_to="img/")
        os_WIN = models.BooleanField(default=True)

class mac(AbstractSoftwareForm):
    def softwareForm(self):
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
        image = models.ImageField(upload_to="img/")
        os_MAC = models.BooleanField(default=True)

class nix(AbstractSoftwareForm):
    def softwareForm(self):
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
        image = models.ImageField(upload_to="img/")
        os_NIX = models.BooleanField(default=True)

registry = Registry(AbstractSoftwareForm)
registry.register(win)
registry.register(mac)
registry.register(nix)

class SubmittedSoftware(models.Model):
    submissionform = StrategyField(registry=registry)
    #image = models.URLField(max_length=200)
    # url feild worked to upload to database
    # while image feild works to view image
    # id 1 has imagefield 2 has urlfield