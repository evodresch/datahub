from django import forms
from .models import SPV, Location, Company, Milestones
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_forms.bootstrap import FormActions

# Base form that includes the standard layout setup with crispy forms
class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()

        for field_name in self.fields:
            self.helper.layout.append(
                Div(
                    Field(field_name, css_class='col-md-9'),
                    css_class='form-row'
                )
            )
    class Meta:
        abstract = True  # This Form is not meant to be used directly


class SPVForm(BaseForm):

    def __init__(self, *args, **kwargs):
        super(SPVForm, self).__init__(*args, **kwargs)
        self.fields['projektgesellschaft'].widget.attrs.update({
            'title': """Beschreibung: Vollständiger Name der Projektgesellschaft\nBeispiel: OneSolar Energiepark 204 GmbH & Co. KG\nQuelle: Corporate Finance"""
        })

    class Meta(BaseForm.Meta):
        model = SPV
        exclude = ['location', 'company']  # Exclude the one to one fields

class LocationForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Location
        fields = '__all__'  # List of model fields you want to include in the form

class CompanyForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Company
        fields = '__all__'  # List of model fields you want to include in the form


class MilestonesForm(BaseForm):
    class Meta(BaseForm.Meta):
        model = Milestones
        fields = '__all__'  # List of model fields you want to include in the form

    def __init__(self, *args, **kwargs):
        super(MilestonesForm, self).__init__(*args, **kwargs)
        # Apply DateInput widget to all DateField instances in the form
        for field_name, field in self.fields.items():
            if isinstance(field, forms.DateField):
                field.widget = forms.DateInput(attrs={
                    'type': 'date',  # Ensures the use of the HTML5 date picker
                    'class': 'form-control',  # Bootstrap class for styling
                    'placeholder': 'Select a date'  # Optional placeholder
                })