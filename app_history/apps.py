from django.apps import AppConfig


class AppHistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_history'

    def ready(self):
        import app_history.signals