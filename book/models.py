from django.db import models

cover = (
    ("H", "HARD"),
    ("S", "SOFT")
)


class Book(models.Model):
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Cover = models.CharField(max_length=4, choices=cover)
    Inventory = models.PositiveIntegerField()
    Daily_fee = models.DecimalField()

    def __str__(self):
        return f"{self.Title}"

