from django import forms
from .models import SPV, Location


class SPVForm(forms.ModelForm):
    class Meta:
        model = SPV
        exclude = ['location']  # Exclude the location field


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'  # List of model fields you want to include in the form
