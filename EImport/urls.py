from django.conf.urls import url
from django.contrib import admin
from homepage import *
urlpatterns = [
       url(r'^index/$', index,name='index'),

]
from django.conf.urls import url
from django.contrib import admin
from views import *
urlpatterns = [
       url(r'^index/$', index,name='index'),

]
