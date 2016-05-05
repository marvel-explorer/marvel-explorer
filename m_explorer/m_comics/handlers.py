from __future__ import unicode_literals
from django.conf import settings
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import ReadingList
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_readinglist(sender, **kwargs):
    instance = kwargs.get('instance', None)
    if instance is not None:
        try:
            new_list = ReadingList(owner=instance)
            new_list.save()
        except (KeyError, ValueError):
            msg = ''
            logger.error(msg.format(instance))


@receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
def remove_user_reading_list(sender, **kwargs):
    instance = kwargs.get('instance', None)
    try:
        instance.readinglist.delete()
    except (KeyError, AttributeError):
        msg = ''
        logger.warn(msg.format(instance))
