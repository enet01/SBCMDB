from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r'^list/', serverlist),
    url(r'^serverList/$', serverlist)
    url(r'^service/(\d{1,3})', service)
]
