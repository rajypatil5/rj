from django import forms
from .models import registrationModel

class registrationForm(forms.ModelForm):
    class Meta:
        model=registrationModel
        fields='__all__'
