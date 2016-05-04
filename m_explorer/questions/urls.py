"""URl routes for the character realated functions."""
from django.conf.urls import url
from .views import GetRandom20

urlpatterns = [
    url(r'^$', GetRandom20.as_view()),
]
