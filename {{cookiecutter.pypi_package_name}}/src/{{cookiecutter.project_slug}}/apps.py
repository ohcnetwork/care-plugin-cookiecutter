from django.apps import AppConfig


PLUGIN_NAME = "{{ cookiecutter.project_slug }}"


class CareAiConfig(AppConfig):
    name = PLUGIN_NAME

    def ready(self):
        pass
