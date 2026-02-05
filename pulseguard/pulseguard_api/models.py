from django.db import models

# Create your models here.

class PopulationStats(models.Model):
    """Analytical table for storing population statistics"""
    avg_age = models.FloatField()
