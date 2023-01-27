from django.db import models
from django.contrib.auth.models import User


class PhotoBook(models.Model):
    title = models.CharField('Name', max_length=250)
    image = models.ImageField(upload_to='photo_books/files/covers')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/forum/{self.id}"

    class Meta:
        verbose_name = 'PhotoBook'
        verbose_name_plural = 'Site PhotoBook'


class PhotoBookPortfolio(models.Model):
    image = models.ImageField(upload_to='photo_books/files/covers')
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    cut = models.ForeignKey(PhotoBook, on_delete=models.CASCADE)


class PhotoBookComment(models.Model):
    full_text = models.TextField('FullText', blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    cut = models.ForeignKey(PhotoBook, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_text