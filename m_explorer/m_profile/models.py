from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


class ActiveUserManager(models.Manager):
    def get_queryset(self):
        qs = super(ActiveUserManager, self).get_queryset()
        return qs.filter(user__is_active__exact=True)


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

    objects = models.Manager()
    active = ActiveUserManager()

    def __str__(self):
        return self.user
