from django import forms

class SearchForm(forms.Form):
    keyword = forms.CharField(label='Tìm kiếm', max_length=100)