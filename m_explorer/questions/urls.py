"""URl routes for the character realated functions."""
from django.conf.urls import url
from .views import GetHeros, GetRandom20

urlpatterns = [
    url(r'^$', GetHeros.as_view()),
    url(r'^random20$', GetRandom20.as_view()),
]
