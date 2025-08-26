from django.apps import AppConfig


class AutomationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
<<<<<<< HEAD:automations/apps.py
    name = 'automations'
    
    def ready(self):
        import automations.signals
=======
    name = 'apps.automations'
    
    def ready(self):
        import apps.automations.signals
>>>>>>> f67fec8c536cd79bdb7a2eeba72fda701318a54d:apps/automations/apps.py
