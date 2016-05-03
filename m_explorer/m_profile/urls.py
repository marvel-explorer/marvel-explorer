from django.conf.urls import url, include
from .views import UserList, UserDetail

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', UserDetail.as_view()),
]
