
from django.conf.urls import url
from django.contrib import admin
from homepage.views import index
from django.conf.urls import url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index,name='index'),
    url(r'^upload/$', 'views.uploadfile', name="import_uploadfile"),

]
