from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from worldOfSpeed.profiles.validators import validate_username_only_alnums_and_underscore


class Profile(models.Model):
    MAX_PROFILE_LENGTH: int = 15
    MIN_PROFILE_LENGTH: int = 3

    MIN_AGE: int = 21

    MAX_PASSWORD_LENGTH: int = 20

    MAX_FIRST_NAME_LENGTH: int = 25
    MAX_LAST_NAME_LENGTH: int = 25

    username = models.CharField(
        max_length=MAX_PROFILE_LENGTH,
        validators=[
            MinLengthValidator(MIN_PROFILE_LENGTH, "Username must be at least 3 chars long!"),
            validate_username_only_alnums_and_underscore,
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        help_text="Age requirement: 21 years and above.",
        validators=[
            MinValueValidator(MIN_AGE),
        ],
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
