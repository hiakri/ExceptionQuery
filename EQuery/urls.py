from django.conf.urls import url
from django.contrib import admin
from homepage.views import index
from EQuery import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index,name='index'),
    url(r'^exception_query/$', views.exception_query),
    url(r'^query/$',views.query_result),
]
