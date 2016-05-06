"""View module for the find a hero display."""
from .models import Character
from .serializers import CharacterSerializer
from rest_framework import generics
from m_comics.serializers import ComicSerializer
from rest_framework.response import Response
from retrieve import api_call


class GetRandom20(generics.ListAPIView):
    """Send JSON of a random 20 characters."""

    queryset = Character.objects.all().exclude(powers='').order_by('?')[:20]
    serializer_class = CharacterSerializer


class GetHeros(generics.ListAPIView):
    """Send JSON of all characters."""

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class ComicsByHeroAPIView(generics.ListAPIView):
    """Get Character's comics by their primary key"""
    serializer_class = ComicSerializer

    def get(self, request, *args, **kwargs):
        character = Character.objects.filter(marvel_id=kwargs['pk'])[0]
        comics = character.comics.all()
        if len(comics) < character.total_comics:
            api_call(kwargs['pk'])
        self.queryset = character.comics.all()
        return self.list(request, *args, **kwargs)
