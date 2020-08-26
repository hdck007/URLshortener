from django import forms
from .models import BigUrl

class URLform(forms.ModelForm):
    class Meta:
        model = BigUrl
        fields = ['inputurl',]