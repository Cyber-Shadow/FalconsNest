from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^$', views.login, name="login"),
    url(r'^auth/$', views.auth_view),
    url(r'^logout/$', views.logout),
    url(r'^yournest/', views.yournest),
    url(r'^unauthorised/', views.unauthorisedpage),
    url(r'^register/$', views.register_page),
    url(r'^chris/$', views.chris),
    url(r'^authr/$', views.register_user),
    url(r'^register_success/$', views.register_success),
    url(r'^hanyuan/$', views.hanyuan),
    url(r'^order/$', views.order),
    url(r'^logout/$', views.logout),
    url(r'^firstlogin/$', views.firstlogin),
    url(r'^links/$', views.schoollinks),
]
