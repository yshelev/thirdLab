from django.apps import AppConfig


class CsgorunConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'csgorun'

    def ready(self):
        import csgorun.signals
