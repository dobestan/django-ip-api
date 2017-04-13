from django.contrib import admin

from iptables.models import Log


class LogModelInline(admin.TabularInline):
    model = Log
    can_delete = False
    extra = 0
    max_num = 10

    readonly_fields = (
        "id",
        "created_at",
    )


@admin.register(Log)
class LogModelAdmin(admin.ModelAdmin):

    readonly_fields = (
        "id",
        "created_at",
    )

    list_display = admin.ModelAdmin.list_display + (
        "id",
        "ip",

        "created_at",
    )

    list_filter = admin.ModelAdmin.list_filter + (
        "created_at",
    )

    search_fields = admin.ModelAdmin.search_fields + (
        "ip__ip_address",
    )
