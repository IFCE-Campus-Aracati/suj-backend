"""Serializadores do blog."""
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import serializers

from blog import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de user."""

    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
        )
        read_only_fields = ("username", "first_name", "last_name")


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
            "comentarios",
        )
        read_only_fields = (
            "autor",
            "pub_date",
            "visualizacoes",
        )

    def create(self, validated_data):
        "Adiciona o usuário autenticado e a timestamp."
        user = self.context["request"].user
        validated_data["autor"] = user
        validated_data["pub_date"] = timezone.now()
        validated_data["visualizacoes"] = 0
        return super().create(validated_data)


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de categorias."""

    class Meta:
        model = models.Categoria
        fields = ("descricao",)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de tags."""

    class Meta:
        model = models.Tag
        fields = ("label",)


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    """Serializador de comentários."""

    class Meta:
        model = models.Comentario
        fields = (
            "autor",
            "post",
            "com_date",
            "texto",
        )

        read_only_fields = (
            "autor",
            "com_date",
        )

    def create(self, validated_data):
        "Adiciona o autor e a timestamp."
        user = self.context["request"].user
        validated_data["autor"] = user
        validated_data["com_date"] = timezone.now()
        return super().create(validated_data)
