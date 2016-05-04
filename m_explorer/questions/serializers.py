"""Character serializers."""
from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):
    """Serializer for Character retreival."""

    class Meta:
        """Define fields to send."""

        model = Character
        fields = ('marvel_id', 'name', 'real_name', 'description',
                  'thumbnail', 'gender', 'pob', 'citizenship', 'occupation',
                  'powers', 'total_comics', 'golden', 'silver', 'bronze',
                  'dark', 'modern', 'hair', 'eyes', 'first_appearance',
                  'identity_status', 'aliases', 'weight', 'height',
                  'group_aff', 'paraphernalia', 'education', 'abilities',
                  'weapons', 'origin')
