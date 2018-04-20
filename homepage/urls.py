# -*-coding:utf-8 -*-
from django.conf.urls import url
from homepage.views import index,toupload,toexception_query,toshow

urlpatterns = [

    url(r'^index/$', index, name='index'),
    url(r'^toupload/$', toupload, name='toupload'),
    url(r'^toexceptionquery/$', toexception_query, name='toexceptionquery'),
    url(r'^toshow/$', toshow, name='toshow'),

]
