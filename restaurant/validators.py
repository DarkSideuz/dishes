from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if not re.match(r'^\+?[0-9]*$', value):
        raise ValidationError('Phone number must be numeric and can start with a +.')