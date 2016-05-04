"""URl routes for the character realated functions."""
from django.conf.urls import url
from .views import GetHeros

urlpatterns = [
    url(r'^$', GetHeros .as_view()),
]
