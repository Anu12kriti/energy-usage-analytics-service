from django.db import models

from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=255)
    utility = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name


class EnergyReading(models.Model):
    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        related_name="energy_readings"
    )

    timestamp = models.DateTimeField()

    imported_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    exported_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    solar_generation_kwh = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.site.name} - {self.timestamp}"
