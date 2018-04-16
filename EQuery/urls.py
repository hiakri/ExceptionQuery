# -*-coding:utf-8 -*-
from django.conf.urls import url
from homepage.views import index
from EQuery import views
urlpatterns = [

    url(r'^index/$', index,name='index'),
    url(r'^exception_query/$', views.exception_query),
    url(r'^query/$',views.query_result),
]
