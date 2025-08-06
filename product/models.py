from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Author(models.Model):
    name = models.CharField(max_length=64)
    bio = models.TextField(null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    AVAILABLE = "available"
    SOLDOUT = "soldout"

    status_list = [
        (AVAILABLE, "Available"),
        (SOLDOUT, "Sold out"),
    ]

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True
    )

    name = models.CharField(max_length=64)
    publication_year = models.DateField()
    pages = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.1),
            MaxValueValidator(1000)
        ]
    )
    status = models.CharField(
        choices=status_list,
        null=True,
        default=SOLDOUT
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}({self.publication_year})"
