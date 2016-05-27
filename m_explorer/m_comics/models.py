from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
# from questions.models import Character


@python_2_unicode_compatible
class Comic(models.Model):
    """
    Comic model for individual comics saved
    to the user's coimc list model
    """
    characters = models.ManyToManyField(
        'questions.Character',
        related_name='comics'
    )
    marvel_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, null=True)
    issue_number = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=10000, null=True)
    upc = models.CharField(max_length=50, null=True)
    page_count = models.IntegerField(null=True)
    _format = models.CharField(max_length=50, null=True)
    detail_url = models.URLField(max_length=255, null=True)
    series = models.CharField(max_length=500, null=True)
    purchase_url = models.URLField(max_length=255, null=True)
    purchase_date = models.DateTimeField(null=True)
    str_pur_date = models.CharField(max_length=15, null=True)
    thumbnail = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ReadingList(models.Model):
    """
    The model for a user's list of comics
    to be read.
    """
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='readinglist'
    )
    comics = models.ManyToManyField(
        Comic,
        through='Membership'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner)


@python_2_unicode_compatible
class Membership(models.Model):
    comic = models.ForeignKey(
        Comic,
        on_delete=models.CASCADE
    )
    readinglist = models.ForeignKey(
        ReadingList,
        on_delete=models.CASCADE,
        related_name='list_membership'
    )
    read = models.BooleanField(default=False)

    def __str__(self):
        return str(self.read)
