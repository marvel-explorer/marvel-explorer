from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


@python_2_unicode_compatible
class ReadingList(models.Model):
    """
    The model for a user's list of comics
    to be read.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='readinglist')
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    comics = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lists')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Comic(models.Model):
    """
    Comic model for individual comics saved
    to the user's coimc list model
    """
    marvel_id = models.IntigerField()
    title = models.CharField()
    characters = models.ManyToManyField(Character)
    issue_number = models.IntigerField()
    description = models.CharField()
    isbn = models.CharField()
    page_count = models.IntigerField()
    url = models.URLField()
    series = models.IntigerField()
    purchase = models.URLField()
    read = models.BooleanField()

    def __str__(self):
        return self.title
