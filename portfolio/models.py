from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/files/covers')


class Portfolio(models.Model):
    image_url = models.ImageField(upload_to='portfolio/files/covers')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)