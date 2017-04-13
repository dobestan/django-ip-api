from django.db import models


class IpManager(models.Manager):
    pass


class Ip(models.Model):

    objects = IpManager()

    ip_address = models.GenericIPAddressField(
        verbose_name="IP 주소",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일",
    )

    class Meta:
        verbose_name = "IP Address"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address
