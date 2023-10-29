from django import forms
from .models import BPost

class NewPostForm(forms.ModelForm):
    class Meta:
        model = BPost
        fields = ['title', 'text', 'author', 'status']
        