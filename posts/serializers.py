from rest_framework import serializers

from posts.models import Comentario, Post, Tag


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["label"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            "url",
            "titulo",
            "texto",
            "data",
            "tags",
            "comentarios",
        ]


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ["post", "texto", "nome", "data"]
