# This displays the column fields that need to be filled in with data
from django import forms
from .models import Calculation

class calculationForm(forms.ModelForm):
    class Meta:
        model=Calculation
        fields=['principal','rate','time']
        