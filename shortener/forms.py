from django import forms
from django.utils.translation import gettext_lazy as _
from shortener.models import Url


class UrlShortenerForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ('url',)
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://www.example.com/search?channel=fs&client=ubuntu&q=zabawne+koty',
                'required': True,
            }),
        }