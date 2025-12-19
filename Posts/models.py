from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add = True)
    banner = CloudinaryField("banner")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.title