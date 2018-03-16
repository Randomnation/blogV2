from django import forms
from .models import Post, Comment, Categories
from ckeditor.widgets import CKEditorWidget
from functools import partial

DateInput = partial(forms.DateInput, {'id': 'datepicker'})


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'type', 'categories', 'text',)


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Comment
        fields = ('author', 'text')


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('title', 'slug', 'description')