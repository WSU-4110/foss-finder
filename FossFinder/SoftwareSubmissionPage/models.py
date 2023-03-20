from django.db import models
from django.contrib.auth.models import User #For Assignment 4
from django.db.models import Avg #For Assignment 4

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

class Post(models.Model): #Here and below is for Assignment 4
    header = models.CharField(max_length=100, default="Header")
    text = models.TextField()

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    def __str__(self):
        return f"{self.header}: {self.average_rating()}"

singleton1 = Post()
new_singleton1 = Post()

print(singleton1 is new_singleton1)
 
singleton1.singl_variable = "Singleton Variable"
print(new_singleton1.singl_variable)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"
    
singleton2 = Rating()
new_singleton2 = Rating()

print(singleton2 is new_singleton2)
 
singleton2.singl_variable = "Singleton Variable"
print(new_singleton2.singl_variable)