from django.conf.urls import url, include
from rest_framework.authtoken import views
from .views import CreateUser, UpdateUser

urlpatterns = [
    url(r'^new$', CreateUser.as_view()),
    url(r'^signin$', views.obtain_auth_token),
    url(r'^(?P<pk>[0-9]+)$', UpdateUser.as_view()),
    url(r'^(?P<pk>[0-9]+)/comics', include('m_comics.urls')),
]
