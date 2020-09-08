from django.apps import AppConfig


class BroadapiConfig(AppConfig):
    name = 'broadapi'

    def ready(self):
        import broadapi.signals
