from .models import Blog
from django.forms import ModelForm
from django import forms

class BlogCreationForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter title.',
        'class': 'form-control',
        'rows': '2'
    }))


    class Meta:
        model = Blog
        fields = ['title', 'content', 'private']