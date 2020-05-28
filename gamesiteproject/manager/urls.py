from django.urls import path, re_path, include
from . import views 

urlpatterns = [

    path('panel/manager/list/', views.manager_list, name='manager_list'),
    re_path(r'^panel/manager/del/(?P<pk>\d+)/$', views.manager_del, name='manager_del'),
    path('panel/manager/group/', views.manager_group, name='manager_group'),
    path('panel/manager/perms/', views.manager_perms, name='manager_perms'),
    re_path(r'^panel/manager/group/add/$', views.manager_group_add, name='manager_group_add'),
    re_path(r'^panel/manager/group/del/(?P<name>.*)/$', views.manager_group_del, name='manager_group_del'),
    re_path(r'^panel/manager/group/show/(?P<pk>\d+)/$', views.users_groups, name='users_groups'),
    re_path(r'^panel/manager/perms/show/(?P<pk>\d+)/$', views.users_perms, name='users_perms'),
    re_path(r'^panel/manager/addtogroup/(?P<pk>\d+)/$', views.add_users_to_groups, name='add_users_to_groups'),
    re_path(r'^panel/manager/delgroup/(?P<pk>\d+)/(?P<name>.*)/$', views.del_users_to_groups, name='del_users_to_groups'),
    re_path(r'^panel/manager/perms/del/(?P<name>.*)/$', views.manager_perms_del, name='manager_perms_del'),
    path('panel/manager/perms/add/', views.manager_perms_add, name='manager_perms_add'),
    re_path(r'^panel/manager/delperm/(?P<pk>\d+)/(?P<name>.*)/$', views.users_perms_del, name='users_perms_del'),
    re_path(r'^panel/manager/addperm/(?P<pk>\d+)/$', views.users_perms_add, name='users_perms_add'),
    re_path(r'^panel/manager/addpermtogroup/(?P<name>.*)/$', views.groups_perms, name='groups_perms'),
    re_path(r'^panel/manager/group/delperms/(?P<gname>.*)/(?P<name>.*)/$', views.groups_perms_del, name='groups_perms_del'),
    re_path(r'^panel/manager/group/addperms/(?P<name>.*)/$', views.groups_perms_add, name='groups_perms_add'),
]