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
                  'upc',
                  'page_count',
                  'detail_url',
                  'series',
                  'purchase_url',
                  'read',
                  'purchase_date')


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = ('owner',
                  'comics',
                  'date_created',
                  'last_modified')
