from profile import Profile

from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class SendForm(forms.ModelForm):
    class Meta:
        model = Send
        fields = '__all__'

class TableForm(forms.ModelForm):
     class Meta:
        model = Table
        fields = '__all__'