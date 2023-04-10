"""Configuração do módulo."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Configurações do app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "posts"
