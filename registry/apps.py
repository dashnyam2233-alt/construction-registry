from django.apps import AppConfig


class RegistryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "registry"

    def ready(self):
        # ✅ Banner/PublicPost admin upload + unregister/register safe
        from . import admin_community  # noqa
