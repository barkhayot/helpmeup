from django import forms
from django.forms import ModelForm
from . models import testCHART, testCHART_DATA





class TestCHARTForm(ModelForm):

    chart_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter the title of your ChartDATA.',
        'type': 'text',
        'class': 'form-control'
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter the description of your ChartDATA.',
        'type': 'text',
        'class': 'form-control'
    }))

    class Meta:
        model = testCHART
        fields = ['chart_name', 'description']


class TestCHART_DATAForm(ModelForm):
    class Meta:
        model = testCHART_DATA
        fields = ['data_name', 'data']

        
    data_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
        'type': 'text',
        'class': 'form-control'
    }))

    data = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Value',
        'type': 'number',
        'class': 'form-control',
        'col': '10'
    }))