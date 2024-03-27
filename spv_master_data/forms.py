from django import forms
from .models import SPV, Location

class SPVForm(forms.ModelForm):
    class Meta:
        model = SPV
        fields = ['projektgesellschaft', 'onesolar_id', 'name']  # List of model fields you want to include in the form

class SPVLocationForm(forms.ModelForm):
    # Location fields
    plz = forms.CharField(max_length=5, )
    gemeinde = forms.CharField(max_length=255)
    gemarkung = forms.CharField(max_length=255)
    flurstuecke = forms.CharField(max_length=50)
    breitengrad = forms.DecimalField(max_digits=9, decimal_places=6)
    laengengrad = forms.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        model = SPV
        fields = ['projektgesellschaft', 'onesolar_id', 'name']