"""Configurações para o painel admin."""
from django.contrib import admin

from blog import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Categoria)
admin.site.register(models.Tag)
admin.site.register(models.Comentario)
