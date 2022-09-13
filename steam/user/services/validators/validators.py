import re

from django.core.exceptions import ValidationError


def validate_phone_number(value):
    match = re.fullmatch(r'^(\+375|80)(29|25|44|33)(\d{3})(\d{2})(\d{2})$', value)
    if not match:
        raise ValidationError(f"{value} is not a phone number")