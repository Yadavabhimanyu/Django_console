from django.apps import AppConfig


class AvionicsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'avionics_app'

    # def ready(self):
    #     from jobs import updater
    #     updater.start()
