from django import forms
from .models import Place

class Post(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title', 'image', 'body']