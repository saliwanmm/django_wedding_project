from django import forms
from .models import PhotoBook


class PhotoBookForm(forms.ModelForm):
    class Meta:
        model = PhotoBook
        fields = ("title", "image")