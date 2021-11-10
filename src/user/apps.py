from django.apps import AppConfig
from django.db.models.signals import post_migrate
# from user.management import create_superuser


class UserConfig(AppConfig):
    name = 'user'

    # def ready(self):
    #     post_migrate.connect(
    #         create_superuser
    #     )
