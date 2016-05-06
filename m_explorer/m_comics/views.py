from .serializers import ComicSerializer
from rest_framework import permissions
from m_profile.permissions import IsObjectOwner
from rest_framework import (
    authentication,
    generics,
    )
from .models import Comic, Membership
from rest_framework import status
from rest_framework.response import Response


class UserComicsCreate(generics.ListCreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    serializer_class = ComicSerializer

    def get_queryset(self):
        user = self.request.user
        return Comic.objects.filter(readinglist__owner__exact=user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # import pdb; pdb.set_trace()
        comic = serializer.save()
        m1 = Membership(comic=comic, readinglist=request.user.readinglist)
        m1.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserComicsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    serializer_class = ComicSerializer

    def get_queryset(self):
        user = self.request.user
        return Comic.objects.filter(readinglist__owner__exact=user)
