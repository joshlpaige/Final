from django.urls import path, re_path, include
from . import views

urlpatterns = [

    path('panel/trending/', views.trending_add, name='trending_add'),
    re_path(r'^panel/trending/del/(?P<pk>\d+)/$', views.trending_del, name='trending_del'),
    re_path(r'^panel/trending/edit/(?P<pk>\d+)/$', views.trending_edit, name='trending_edit'),

]