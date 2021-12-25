from django import forms
from django.forms import ModelForm
from .models import NOTE

class NoteCreateForm(ModelForm):
   content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter your note here.',
        'class': 'form-control',
        'rows':'5'
    }))


   class Meta:
      model = NOTE
      fields = ['content']