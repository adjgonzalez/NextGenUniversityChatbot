from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    # Registering the signal to the app
    def ready(self):
        # Import signals so they get registered
        import users.signals # IF THIS DISSAPEARS FOR THE 5TH TIME, ILL LOSE IT
        print(users.signals)
