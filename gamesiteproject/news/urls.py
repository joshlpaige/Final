from django.urls import path, re_path, include
from . import views 

urlpatterns = [

    
    re_path(r'^news/(?P<word>.*)/$', views.news_detail, name='news_detail'),
    path('panel/news/list/', views.news_list, name='news_list'),
    path('panel/news/add', views.news_add, name='news_add'),
    re_path(r'^panel/news/del/(?P<pk>\d+)', views.news_delete, name='news_delete'),
    re_path(r'^panel/news/edit/(?P<pk>\d+)', views.news_edit, name='news_edit'),
    re_path(r'^urls/(?P<pk>\d+)/$', views.news_detail_short, name='news_detail_short'),
    re_path(r'^all/news/(?P<word>.*)/$', views.news_all_show, name='news_all_show'),

]