from django.conf.urls import url
from django.contrib import admin
from homepage.views import index
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index,name='index'),

]
