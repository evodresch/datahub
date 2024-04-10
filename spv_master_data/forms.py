from django import forms
from .models import SPV, Location, Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import FormActions


class SPVForm(forms.ModelForm):
    class Meta:
        model = SPV
        exclude = ['location', 'company']  # Exclude the one to one fields


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'  # List of model fields you want to include in the form

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'  # List of model fields you want to include in the form
