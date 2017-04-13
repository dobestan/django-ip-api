from django.apps import AppConfig


class IptablesAppConfig(AppConfig):
    name = "iptables"

    def ready(self):
        pass
