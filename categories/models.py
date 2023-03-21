from django.db import models

class Category(models.Model):
    word_processor = models.CharField(max_length=100)
    spreadsheet_editor = models.CharField(max_length=100)
    file_sharing = models.CharField(max_length=100)
    audio_editing = models.CharField(max_length=100)
    graphical_editing = models.CharField(max_length=100)
    antivirus = models.CharField(max_length=100)
    communication = models.CharField(max_length=100)
    disk_burning_software = models.CharField(max_length=100)
    multimedia = models.CharField(max_length=100)
    code_editor = models.CharField(max_length=100)
    other = models.CharField(max_length=100)
