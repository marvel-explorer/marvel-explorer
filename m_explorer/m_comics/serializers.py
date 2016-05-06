from .models import Comic, ReadingList, Membership
from rest_framework import serializers


class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ('read')


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        groups = MembershipSerializer(source='membership_set', many=True)
        fields = (
            'marvel_id',
            'title',
            'characters',
            'issue_number',
            'description',
            'upc',
            'page_count',
            'detail_url',
            'series',
            'purchase_url',
            'purchase_date'
        )


class ReadingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingList
        fields = (
            'owner',
            'comics',
            'date_created',
            'last_modified',
            'read'
        )
