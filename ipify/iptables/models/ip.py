from django.db import models
from django.contrib.postgres.fields import JSONField


class IpManager(models.Manager):

    def get_queryset(self):
        return super(IpManager, self).get_queryset()\
            .prefetch_related("log_set")\


class Ip(models.Model):

    objects = IpManager()

    ip_address = models.GenericIPAddressField(
        verbose_name="IP 주소",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일",
    )

    note = models.CharField(
        max_length=64,
        blank=True,
        null=True,
        verbose_name="비고",
    )

    city = JSONField(
        blank=True,
        null=True,
        verbose_name="GeoIP City Information",
    )

    class Meta:
        verbose_name = "IP 주소"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip_address
