from django import forms
from .models import UserProfile
from functools import partial


DateInput = partial(forms.DateInput, {'id': 'datepicker'})


class ProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=DateInput())

    class Meta:
        model = UserProfile
        fields = {'bio', 'homepage', 'gamer_tag', 'date_of_birth', }