from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
