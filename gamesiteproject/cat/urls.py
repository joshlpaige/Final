from django.urls import path, re_path, include
from . import views 

urlpatterns = [

    
    
    re_path(r'^panel/category/list/$', views.cat_list, name='cat_list'),
    path('panel/category/add', views.cat_add, name='cat_add'),
   


]