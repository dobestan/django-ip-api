from django.contrib import admin

from iptables.models import Ip


@admin.register(Ip)
class IpModelAdmin(admin.ModelAdmin):

    readonly_fields = (
    )

    list_display = admin.ModelAdmin.list_display + (
    )

    list_filter = admin.ModelAdmin.list_filter + (
    )

    search_fields = admin.ModelAdmin.search_fields + (
    )

    inlines = (
    )
