from django import forms
from models import Post

from redactor.widgets import RedactorEditor


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': RedactorEditor(),
        }
        exclude = [
                'comments',
        ]


class SearchForm(forms.Form):
    word = forms.CharField(max_length=10)
