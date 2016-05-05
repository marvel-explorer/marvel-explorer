from django.apps import AppConfig


class MComicsConfig(AppConfig):
    name = 'm_comics'

    def ready(self):
        from m_comics import handlers
