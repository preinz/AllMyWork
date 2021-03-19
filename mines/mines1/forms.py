from profile import Profile

from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'