from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from m_profile.models import MarvelProfile
from m_comics.models import ReadingList
from rest_framework.authtoken.models import Token
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, **kwargs):
    if kwargs.get('created', False):
        instance = kwargs.get('instance', None)
        if instance is not None:
            try:
                new_profile = MarvelProfile(user=instance)
                new_profile.save()
            except (KeyError, ValueError):
                msg = 'Unable to create profile for specified user.'
                logger.error(msg.format(instance))


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, **kwargs):
    instance = kwargs.get('instance', None)
    created = kwargs.get('created', None)
    if created:
        Token.objects.create(user=instance)


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_user_profile(sender, **kwargs):
    instance = kwargs.get('instance', None)
    try:
        instance.profile.delete()
    except (KeyError, AttributeError):
        msg = 'No profile found for that user.  No profile deleted.'
        logger.warn(msg.format(instance))
