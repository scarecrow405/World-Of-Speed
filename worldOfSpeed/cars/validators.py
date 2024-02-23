from django.core.exceptions import ValidationError


def validate_year_between_1999_and_2030(value):
    if value < 1999 or value > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")
