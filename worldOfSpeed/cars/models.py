from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from worldOfSpeed.cars.validators import validate_year_between_1999_and_2030
from worldOfSpeed.profiles.models import Profile


class CarTypes(models.TextChoices):
    RALLY = "Rally"
    OPEN_WHEEL = "Open-wheel"
    KART = "Kart"
    DRAG = "Drag"
    OTHER = "Other"


class Car(models.Model):
    MAX_TYPE_LENGTH: int = 10

    MAX_MODEL_LENGTH: int = 15
    MIN_MODEL_LENGTH: int = 1

    MAX_YEAR: int = 2030
    MIN_YEAR: int = 1999

    MIN_PRICE: float = 1.0

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        choices=CarTypes.choices,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=[
            MinLengthValidator(MIN_MODEL_LENGTH),
        ],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[
            validate_year_between_1999_and_2030,
        ],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        error_messages={
            "unique": "This image URL is already in use! Provide a new one.",
        },
        unique=True,
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=[
            MinValueValidator(MIN_PRICE),
        ],
        null=False,
        blank=False,
    )

    owner = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE,
        related_name="cars",
    )
