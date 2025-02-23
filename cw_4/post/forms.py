from django import forms
from .models import Post, Thread

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'author', 'picture']