from django.urls import path, re_path, include
from . import views 

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('panel/', views.panel, name='panel'),
    path('hacker/', views.hacker, name='hacker'),
    path('slay/', views.slay, name='slay'),
    path('playground/', views.playground, name='playground'),
    path('login/', views.mylogin, name='mylogin'),
    path('logout/', views.mylogout, name='mylogout'),
    path('panel/setting/', views.site_setting, name='site_setting'),
    path('panel/about/setting/', views.about_setting, name='about_setting'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit', views.msgbox, name='msgbox'),
    path('panel/change/pass/', views.change_pass, name='change_pass'),
    path('register/', views.myregister, name='myregister'),
    re_path(r'^all/news/(?P<word>.*)/$', views.news_all_show, name='news_all_show'),

]