from .models import Comic, ReadingList
from rest_framework import serializers


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ('marvel_id',
                  'title',
                  'characters',
                  'issue_number',
                  'description',
                  'isbn',
                  'page_count',
                  'url',
                  'series',
                  'purchase',
                  'read',
                  'purchase_date')


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ('owner',
                  'comics',
                  'date_created',
                  'last_modified')
