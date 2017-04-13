from django.db import models
from django.contrib.postgres.fields import JSONField


class LogManager(models.Manager):

    def get_queryset(self):
        return super(LogManager, self).get_queryset()\
            .select_related("ip")


class Log(models.Model):

    objects = LogManager()

    ip = models.ForeignKey("Ip")

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

    meta = JSONField(
        blank=True,
        null=True,
        verbose_name="HTTP Headers",
        help_text="""
        HttpRequest.META
        """,
    )

    class Meta:
        verbose_name = "IP 로그"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip.ip_address
