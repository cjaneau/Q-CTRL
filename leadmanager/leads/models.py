from django.db import models

class Lead(models.Model):
    name=models.CharField(max_length=100)
    Type=models.CharField(max_length=100, unique=True)
    maximum_rabi_rate=models.IntegerField(blank=False, decimal_places=5)
    polar_angle=models.IntegerField(blank=False, decimal_places=5)