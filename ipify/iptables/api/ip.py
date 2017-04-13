import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from iptables.models import Ip, Log

from ipware.ip import get_real_ip, get_ip


class IpCheckAPIView(APIView):

    def get(self, request, format=None):

        ip_address = get_real_ip(request) or get_ip(request)
        ip, created = Ip.objects.get_or_create(ip_address=ip_address)

        meta = {
            key: value
            for key, value
            in request.META.items()
            if key.startswith("HTTP")
        }
        log = ip.log_set.create(
            meta=meta,
        )

        content = {
            "ip": ip.ip_address,
        }

        return Response(
            content,
            status=status.HTTP_200_OK,
        )
