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

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Character(models.Model):
    """Create Character Stats model for the database."""
    name = models.CharField(max_length=6000, null=False, blank=True)
    real_name = models.CharField(max_length=100, null=False, blank=True)
    marvel_name = models.CharField(max_length=100, null=False, blank=True)
    marvel_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=10000, null=False, blank=True)
    thumbnail = models.CharField(max_length=1000, null=False, blank=True)
    gender = models.CharField(max_length=30, null=False, blank=True)
    pob = models.CharField(max_length=6000, null=False, blank=True)
    citizenship = models.CharField(max_length=500, null=False, blank=True)
    occupation = models.CharField(max_length=6000, null=False, blank=True)
    powers = models.CharField(max_length=10000, null=False, blank=True)
    total_comics = models.IntegerField(blank=True, null=False, default=None)
    golden = models.NullBooleanField(blank=True, null=False, default=None)
    silver = models.NullBooleanField(blank=True, null=False, default=None)
    bronze = models.NullBooleanField(blank=True, null=False, default=None)
    dark = models.NullBooleanField(blank=True, null=False, default=None)
    modern = models.NullBooleanField(blank=True, null=False, default=None)
    hair = models.CharField(max_length=6000, null=False, blank=True)
    eyes = models.CharField(max_length=6000, null=False, blank=True)
    first_appearance = models.CharField(max_length=6000, null=False, blank=True)
    identity_status = models.CharField(max_length=6000, null=False, blank=True)
    aliases = models.CharField(max_length=550, null=False, blank=True)
    weight = models.CharField(max_length=6000, null=False, blank=True)
    height = models.CharField(max_length=6000, null=False, blank=True)
    group_aff = models.CharField(max_length=550, null=False, blank=True)
    paraphernalia = models.CharField(max_length=10000, null=False, blank=True)
    education = models.CharField(max_length=2000, null=False, blank=True)
    abilities = models.CharField(max_length=10000, null=False, blank=True)
    weapons = models.CharField(max_length=10000, null=False, blank=True)
    origin = models.CharField(max_length=550, null=False, blank=True)

    objects = CharacterManager()

    class Meta():
        app_label = 'questions'

    def __str__(self):
        return self.name
