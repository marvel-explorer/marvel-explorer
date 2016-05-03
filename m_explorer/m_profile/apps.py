from django.apps import AppConfig


class MProfileConfig(AppConfig):
    name = 'm_profile'

    def ready(self):
        from m_profile import handlers
