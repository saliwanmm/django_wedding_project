from django import forms


class UserSearchForm(forms.Form):
    last_name = forms.CharField(max_length=100)