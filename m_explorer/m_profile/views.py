from django.contrib.auth.models import User
from m_profile.models import MarvelProfile
from m_comics.models import Comic
from m_profile.serializers import UserSerializer, ProfileSerializer
from m_comics.serializers import ComicSerializer
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateProfile(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = MarvelProfile.objects.all()
    serializer_class = ProfileSerializer


class UserComics(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
