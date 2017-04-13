from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.gis.geoip2 import GeoIP2

from iptables.models import Ip


@receiver(post_save, sender=Ip)
def post_save_ip(sender, instance, created, **kwargs):
    if created:
        try:
            geoip = GeoIP2()
            city = geoip.city(instance.ip_address)
            instance.city = city
            instance.save()
        except:
            pass
