from django.urls import path, re_path, include
from . import views 

urlpatterns = [

    path('panel/manager/list/', views.manager_list, name='manager_list'),
    re_path(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),
    path('panel/manager/group/', views.manager_group, name='manager_group'),
    path('panel/manager/group/add/', views.manager_group_add, name='manager_group_add'),
    re_path(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),
    re_path(r'^panel/manager/group/show/(?P<pk>\d+)/$', views.users_groups, name='users_groups'),
    re_path(r'^panel/manager/addtogroup/(?P<pk>\d+)/$', views.add_users_to_groups, name='add_users_to_groups'),
    re_path(r'^panel/manager/delgroup/(?P<pk>\d+)/(?P<name>.*)/$', views.del_users_to_groups, name='del_users_to_groups'),
]