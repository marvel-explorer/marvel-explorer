from django.conf.urls import url
from .views import CreateUser, UpdateUser, UserComics

urlpatterns = [
    url(r'^/new$', CreateUser.as_view()),
    url(r'^(?P<pk>[0-9]+)$', UpdateUser.as_view()),
    url(r'^(?P<pk>[0-9]+)/comics$', UserComics.as_view()),
]
