from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class CharacterManager(models.Manager):
    """Define an Active Profile Manager class."""

    def get_queryset(self):
        """Return a list of all active users."""
        qs = super(CharacterManager, self).get_queryset()
        return qs.all()


@python_2_unicode_compatible
class Character(models.Model):
    """Create Character Stats model for the database."""
    name = models.CharField(max_length=60) # got it
    real_name = models.CharField(max_length=100, blank=True) # got it
    marvel_name = models.CharField(max_length=100) # api
    marvel_id = models.CharField(max_length=20, primary_key=True) # api
    description = models.CharField(max_length=250) # api
    thumbnail = models.CharField(max_length=250) # api
    gender = models.CharField(max_length=30) # create counting function
    pob = models.CharField(max_length=200, blank=True) # got it
    # species = models.CharField(max_length=60, blank=True) # wikipedia stretch
    # race = models.CharField(max_length=70, blank=True) # wikipedia stretch
    citizenship = models.CharField(max_length=90, blank=True) # I have
    occupation = models.CharField(max_length=200, blank=True) # I have
    powers = models.CharFild(max_length=200, blank=True) # wikipedia stretch
    comics = models.CharField(max_length=250)
    total_comics = models.IntegerField()  # api
    golden = models.NullBooleanField() # api analysis
    silver = models.NullBooleanField() # api analysis
    bronze = models.NullBooleanField() # api analysis
    dark = models.NullBooleanField() # api analysis
    modern = models.NullBooleanField() # api analysis
    hair = models.CharField(max_length=30)
    eyes = models.CharField(max_length=30)
    first_appearance = models.CharField(max_length=60)
    identity_status = models.CharField(max_length=60)
    aliases = models.CharField(max_length=250)
    weight = models.CharField(max_length=60)
    height = models.CharField(max_length=60)
    group_aff = models.CharField(max_length=250)
    paraphernalia = models.CharField(max_length=250)
    education = models.CharField(max_length=60)
    occupation = models.CharField(max_length=250)
    abilities = models.CharField(max_length=250)
    weapons = models.CharField(max_length=250)
    origin = models.CharField(max_length=250)

    objects = CharacterManager()
