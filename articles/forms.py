from django import forms
from .models import Questions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ["description", "cat_category"]


class SearchInterviewForm(forms.Form):
    username = forms.CharField(max_length=100)