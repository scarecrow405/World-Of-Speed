from django.core.exceptions import ValidationError


def validate_username_only_alnums_and_underscore(value):
    if not value.isalnum() and "_" not in value:
        raise ValidationError("Username must contain only letters, digits, and underscores!")
