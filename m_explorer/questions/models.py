from __future__ import unicode_literals

from django.db import models


class Character(models.Model):
    """Create Character Stats model for the database."""
    name = models.CharField(max_length=60)
    alter_ego = models.CharField(max_length=100, blank=True)
    marvel_name = models.CharField(max_length=100)
    marvel_id = models.CharField(max_length=20)
    description = models.CharField(max_length=250)
    thumbnail = models.CharField(max_length=250)
    gender = models.CharField(max_length=30)
    pob = models.CharField(max_length=200, blank=True)
    species = models.CharField(max_length=60, blank=True)
    race = models.CharField(max_length=70, blank=True)
    nationality = models.CharField(max_length=90, blank=True)
    occupation = models.CharField(max_length=200, blank=True)
    powers = models.CharField(max_length=200, blank=True)
    series = models.CharField(max_length=250)
