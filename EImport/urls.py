

# -*-coding:utf-8 -*-
from homepage.views import index
from django.conf.urls import url
from django import views
urlpatterns = [

    url(r'^index/$', index, name='index'),
    url(r'^upload/$', views.uploadfile, name='import_uploadfile'),

]
