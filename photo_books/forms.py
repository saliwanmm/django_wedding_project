from django import forms
from .models import PhotoBook, PhotoBookPortfolio


class PhotoBookForm(forms.ModelForm):
    class Meta:
        model = PhotoBook
        fields = ("title", "image")


class PhotoBookPortfolioForm(forms.ModelForm):
    class Meta:
        model = PhotoBookPortfolio
        fields = ("image",)