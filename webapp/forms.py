from django.forms import ModelForm
from django import forms
from django.core.validators import MaxValueValidator

class Order(forms.Form):
    name = forms.CharField(max_length=30)
    amount = models.PositiveIntegerField(min_value=0, validators=[MaxValueValidator(3),]
    
class addorderform(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    value = 0