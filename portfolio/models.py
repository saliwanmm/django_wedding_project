from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/files/covers')


class Portfolio(models.Model):
    image_url = models.ImageField(upload_to='portfolio/files/covers')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)



class PortfolioComment(models.Model):
    full_text = models.TextField('FullText', blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    cut = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_text