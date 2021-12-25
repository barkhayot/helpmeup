from django import forms
from django.forms import ModelForm
from .models import URL_DATA

class LinkCreateForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the title of your Link.',
        'type': 'text',
        'class': 'form-control'
    }))

    url_link = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the url link.',
        'type': 'text',
        'class': 'form-control'
        
    }))

    class Meta:
        model = URL_DATA
        fields = ['title', 'url_link']
