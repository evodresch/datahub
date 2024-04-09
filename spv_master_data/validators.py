# validators.py
from django.core.exceptions import ValidationError
import re

# Validator for the IBAN format
def validate_iban(value):
    if not re.match(r'^[A-Z]{2}\d{2}[A-Z0-9]{1,30}$', value):
        raise ValidationError('Invalid IBAN format. Please enter a valid IBAN.')
    # Add more sophisticated validation logic as needed.
