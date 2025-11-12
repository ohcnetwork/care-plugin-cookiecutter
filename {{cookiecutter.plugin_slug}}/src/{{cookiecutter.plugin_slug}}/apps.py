from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "{{ cookiecutter.plugin_slug }}"


class {{cookiecutter.plugin_name.split(' ')|map('capitalize')|join}}Config(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("{{cookiecutter.plugin_name.capitalize()}}")

    def ready(self):
        import {{ cookiecutter.plugin_slug }}.signals  # noqa F401
