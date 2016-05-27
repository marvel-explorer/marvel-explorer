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
        # import pdb; pdb.set_trace()
        comic_id = request.data['marvel_id']
        comic_id = int(comic_id)
        comic = Comic.objects.filter(marvel_id=comic_id)[0]
        m1 = Membership(comic=comic, readinglist=request.user.readinglist)
        m1.save()
        return Response(status=status.HTTP_201_CREATED)


class UserComicsUpdate(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner,)

    serializer_class = ComicSerializer

    def get_queryset(self):
        user = self.request.user
        return Comic.objects.filter(readinglist__owner__exact=user)