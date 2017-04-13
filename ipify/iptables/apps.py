from django.apps import AppConfig


class IptablesAppConfig(AppConfig):
    name = "iptables"

    def ready(self):
        from iptables.signals.post_save import post_save_ip
