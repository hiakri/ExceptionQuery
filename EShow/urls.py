# -*-coding:utf-8 -*-
from django.conf.urls import url
from homepage.views import index
urlpatterns = [

    url(r'^index/$', index, name='index'),

]
