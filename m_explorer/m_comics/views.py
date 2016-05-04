from .serializers import ComicSerializer, ReadingListSerializer
from rest_framework import permissions
from m_profile.permissions import IsObjectOwner
from rest_framework import authentication
from rest_framework import viewsets


class ComicViewSet(viewsets.ModelViewSet):
    """
    Comprehensive viewset for Comics, providing list, create, retrieve,
    update and destroy actions.
    """
    serializer_class = ComicSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsObjectOwner)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.comics.all()
