from django.contrib.auth.models import User
from m_profile.serializers import ProfileSerializer
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics


class UserList(generics.ListCreateAPIView):

    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
