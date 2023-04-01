from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)
    images = models.ImageField('images')
