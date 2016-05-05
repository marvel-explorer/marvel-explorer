from django.contrib.auth.models import User
from .models import MarvelProfile
from .serializers import UserSerializer, ProfileSerializer
from .permissions import IsObjectOwner
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import generics


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdateUser(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        import pdb; pdb.set_trace()
        return User.objects.get(pk=self.request.user.pk)


class UpdateProfile(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    queryset = MarvelProfile.objects.all()
    serializer_class = ProfileSerializer

    def get_object(self):
        return MarvelProfile.objects.get(pk=self.request.user.pk)
