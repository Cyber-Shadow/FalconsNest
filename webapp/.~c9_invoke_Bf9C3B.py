from django.forms import ModelForm
from django import forms

class Ordername(forms.Form):
    Name = forms.CharField(max_length=100)
    Sh = forms.CharField()