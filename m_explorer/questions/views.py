"""View module for the find a hero display."""
from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics


class GetHeros(generics.ListAPIView):
    """Return the top 20 characters orderd by max."""

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
