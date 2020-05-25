from django.urls import path, re_path, include
from . import views

urlpatterns = [

    path('contact/submit/', views.contact_add, name='contact_add'),
    path('panel/contactform/', views.contact_show, name='contact_show'),
    re_path(r'^panel/contactform/del/(?P<pk>\d+)/$', views.contact_del, name='contact_del'),

]
