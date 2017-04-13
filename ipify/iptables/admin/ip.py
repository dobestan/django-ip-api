from django.contrib import admin

from iptables.models import Ip

from .log import LogModelInline


@admin.register(Ip)
class IpModelAdmin(admin.ModelAdmin):

    readonly_fields = (
    )

    list_display = admin.ModelAdmin.list_display + (
        "id",
        "ip_address",
        "created_at",
    )

    list_filter = admin.ModelAdmin.list_filter + (
        "created_at",
    )

    search_fields = admin.ModelAdmin.search_fields + (
        "ip_address",
    )

    inlines = (
        LogModelInline,
    )
