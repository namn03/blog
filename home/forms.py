from django import forms
from models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
                'comments',
        ]


class SearchForm(forms.Form):
    word = forms.CharField(max_length=10)