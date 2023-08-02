from django.apps import AppConfig


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
    
    # Fix to lack of login and logout logging:
    # def ready(self):
    #    import polls.loglog