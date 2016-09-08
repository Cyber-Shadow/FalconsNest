from django.conf.urls import url
from . import views, auth

urlpatterns = [
    #Pages
    url(r'^hanyuan/$', views.hanyuan),
    url(r'^links/$', views.schoollinks),
    url(r'^settings/$', views.settings),
    url(r'^yournest/', views.yournest),
    url(r'^chris/', views.chris),
    url(r'^menu/', views.menu),
    
    #Actions
    url(r'^addorder/$', views.addorder),
    url(r'^delorder/$', views.delorder),
    #url(r'^addmenu/$', views.addmenu),
    url(r'^order/$', views.order),
    
    #Authenication
    url(r'^$', auth.login),
    url(r'^auth/$', auth.auth_view),
    url(r'^logout/$', auth.logout),
    url(r'^authr/$', auth.register_user),
    url(r'^logout/$', auth.logout),
    url(r'^firstlogin/$', auth.firstlogin),
    url(r'^register_success/$', auth.register_success),
    url(r'^unauthorised/', auth.unauthorisedpage),

]