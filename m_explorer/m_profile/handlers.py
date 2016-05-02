from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from m_profile.models import MarvelProfile
import logging


logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def ensure_user_profile(sender, **kwargs):
    if kwargs.get('created', False):
        try:
            new_profile = MarvelProfile(user=kwargs['instance'])
            new_profile.save()
        except (KeyError, ValueError):
            msg = 'Unable to create profile for specified user.'
            logger.error(msg.format(kwargs['instance']))


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_user_profile(sender, **kwargs):
    try:
        kwargs['instance'].profile.delete()
    except (KeyError, AttributeError):
        msg = 'No profile found for that user.  No profile deleted.'
        logger.warn(msg.format(kwargs['instance']))
