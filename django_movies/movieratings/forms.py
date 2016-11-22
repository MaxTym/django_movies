from django import forms
from .models import Rater, Rating
from django.contrib.auth.models import User


class sign_up(forms.Form):
    sign_up = forms.CharField(label='sign_up', max_length=100)


class RaterForm(forms.ModelForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = Rater
        fields = ['age', 'gender', 'occupation', 'zip_code']

# class RatingForm(forms.ModelForm):
#     class Meta:
#         model = Rating
#         fields = ['rating']
