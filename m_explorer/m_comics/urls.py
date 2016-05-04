from django.conf.urls import url
from .views import ComicViewSet
from rest_framework.urlpatterns import format_suffix_patterns


comic_root = ComicViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', comic_root),
])
