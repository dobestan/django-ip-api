from django.conf.urls import url, include

from iptables.api import *


urlpatterns = [
    url(r'^$', IpCheckAPIView.as_view(), name="ip-check"),
]
