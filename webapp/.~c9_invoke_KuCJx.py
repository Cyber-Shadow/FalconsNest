from django.forms import ModelForm
impor

class Ordername(forms.Form):
    Name = forms.CharField(max_length=100)
    Sh = forms.CharField()