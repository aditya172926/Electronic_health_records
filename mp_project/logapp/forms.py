from django import forms
from .models import *
  
class PresImageForm(forms.Form):
    pres_image = forms.ImageField()