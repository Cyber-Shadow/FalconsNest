from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^$', views.login, name="login"),
]
