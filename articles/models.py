from django.contrib.auth.models import User
from django.db import models


class CategoryQuestions(models.Model):
    description = models.TextField()

    def __str__(self):
        return self.description


class Interviews(models.Model):
    cat_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class Questions(models.Model):
    description = models.TextField(blank=True)
    cat_category = models.ForeignKey(CategoryQuestions, null=False, on_delete=models.CASCADE)
    cat_user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    cat_interview = models.ForeignKey(Interviews, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
