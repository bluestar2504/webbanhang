from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Tìm kiếm', max_length=100)

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))