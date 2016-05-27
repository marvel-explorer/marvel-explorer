from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


@python_2_unicode_compatible
class MarvelProfile(models.Model):
    """
    User profile model attached to Django's
    built-in User model
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='profile')
    location = models.CharField(default='',
                                max_length=255)
    bio = models.TextField(default='')
    fav_hero = models.CharField(default='',
                                max_length=100)

    def __str__(self):
        return str(self.user)
