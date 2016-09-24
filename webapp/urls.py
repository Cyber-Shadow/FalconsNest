from django.conf.urls import url, include
from . import views, auth

urlpatterns = [
    #Pages
    url(r'^hanyuan/$', views.hanyuan),
    url(r'^dirran/$', views.dirran),
    url(r'^links/$', views.schoollinks),
    url(r'^settings/$', views.settings),
    url(r'^yournest/', views.yournest),
    url(r'^chris/', views.chris),
    url(r'^chrismenu/', views.chrismenu),
    url(r'^menu/', views.menu),
    url(r'^error/', views.error),
    url(r'^about/$', views.about),
    url(r'^about/terms', views.terms),
    url(r'^ben/', views.ben),
    
    
    #Actions
    url(r'^addorder/$', views.addorder),
    url(r'^delorder/$', views.delorder),
    url(r'^addmenu/$', views.addmenu), 
    url(r'^delmenu/$', views.delmenu),
    url(r'^order/$', views.order),
    url(r'^faveorder/$', views.faveorder),
    url(r'^quickorder/$', views.quickorder),

    
    #Authenication
    url(r'^$', auth.login),
    url(r'^auth/$', auth.auth_view),
    url(r'^logout/$', auth.logout),
    url(r'^authr/$', auth.register_user),
    url(r'^logout/$', auth.logout),
    url(r'^firstlogin/$', auth.firstlogin),
    url(r'^register_success/$', auth.register_success),
    url(r'^unauthorised/', auth.unauthorisedpage),
    url(r'^changepw/$', auth.changepw),
    #NiceCommentsCraig #Thanks
]