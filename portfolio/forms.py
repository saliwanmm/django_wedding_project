from django.forms import ModelForm
from .models import Movie, Portfolio
from django import forms


class MovieForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()

    class Meta:
        model = Movie
        fields = ['name', 'image']


class PortfolioForm(ModelForm):
    # image_url = forms.ImageField()
    # user = forms.TextInput()

    class Meta:
        model = Portfolio
        fields = ['image_url']