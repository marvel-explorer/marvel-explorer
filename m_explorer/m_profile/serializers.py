from rest_framework import serializers
from m_profile.models import MarvelProfile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarvelProfile
        fields = ()
