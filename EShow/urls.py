# -*-coding:utf-8 -*-
from django.conf.urls import url
from homepage.views import index
from django import views
urlpatterns = [

    url(r'^index/$', index, name='index'),
    url(r'^show/$', views.show, name='show'),
]
