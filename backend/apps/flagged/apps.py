from django.apps import AppConfig


class FlaggedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.apps.flagged'
