"""View module for the find a hero display."""
from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics


class GetRandom20(generics.ListAPIView):
    """Return the top 20 characters orderd by max."""
    queryset = Character.objects.all().exclude(powers='').order_by('?')[:20]
    serializer_class = CharacterSerializer
