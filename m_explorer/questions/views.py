"""View module for the find a hero display."""
from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics


class GetRandom20(generics.ListAPIView):
    """Send JSON of a random 20 characters."""

    queryset = Character.objects.all().exclude(powers='').order_by('?')
    serializer_class = CharacterSerializer


class GetHeros(generics.ListAPIView):
    """Send JSON of all characters."""

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
