from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MarvelProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarvelProfile
        fields = ('bio', 'location')
