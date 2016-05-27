from django.conf.urls import url
from rest_framework.authtoken import views
from .views import CreateUser, UpdateUser, UpdateProfile
from m_comics.views import UserComicsUpdate, UserComicsCreate

urlpatterns = [
    url(r'^signup$', CreateUser.as_view()),
    url(r'^signin$', views.obtain_auth_token),
    url(r'^$', UpdateUser.as_view()),
    url(r'^profile$', UpdateProfile.as_view()),
    url(r'^comics/update$', UserComicsUpdate.as_view()),
    url(r'^comics$', UserComicsCreate.as_view()),
]
