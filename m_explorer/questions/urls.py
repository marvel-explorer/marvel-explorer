"""URl routes for the character realated functions."""
from django.conf.urls import url
from .views import GetHeros, GetRandom20, ComicsByHeroAPIView

urlpatterns = [
    url(r'^$', GetHeros.as_view()),
    url(r'^random20$', GetRandom20.as_view()),
    url(r'^(?P<pk>[0-9]+)/comics$', ComicsByHeroAPIView.as_view())
]
