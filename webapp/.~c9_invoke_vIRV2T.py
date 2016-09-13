from django.conf.urls import url
from . import views, auth

urlpatterns = [
    url(r'^hanyuan/$', views.hanyuan),
    url(r'^order/$', views.order),
    url(r'^links/$', views.schoollinks),
    url(r'^settings/$', views.settings),
    url(r'^addorder/$', views.addorder),
    url(r'^yournest/', views.yournest),
    
    
    
  # url(r'^getmenu/$', auth.getMenu),
    url(r'^$', auth.login),
    url(r'^auth/$', auth.auth_view),
    url(r'^logout/$', auth.logout),
    url(r'^authr/$', auth.register_user),
    url(r'^logout/$', auth.logout),
    url(r'^firstlogin/$', auth.firstlogin),
    url(r'^register_success/$', auth.register_success),
    url(r'^unauthorised/', auth.unauthorisedpage),
    url(r'^register/$', auth.register_page),
]