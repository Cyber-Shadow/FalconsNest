from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^$', views.login, name="login"),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^yournest/', views.yournest),
    url(r'^invalid/$', views.invalid_login),
    url(r'^register/$', views.register_page),
    url(r'^authr/$', views.register_user),
    url(r'^register_success/$', views.register_success),
    url(r'^hanyuan/$', views.hanyuan),
    url(r'^order/$', views.order),
]
