"""Serializadores do blog."""

from rest_framework import serializers

from blog import models


class PostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de Post."""

    class Meta:
        model = models.Post
        fields = (
            "id",
            "titulo",
            "conteudo",
            "pub_date",
            "autor",
            "categoria",
            "tags",
            "visualizacoes",
        )
