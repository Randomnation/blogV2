from django import forms
from .models import Post, Categories
from ckeditor.widgets import CKEditorWidget
from functools import partial
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Field, Submit


DateInput = partial(forms.DateInput, {'id': 'datepicker'})


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('title', 'type', 'categories', 'text',)


class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('title', 'slug', 'description')