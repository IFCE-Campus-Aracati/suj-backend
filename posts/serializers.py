from rest_framework import serializers
from django.contrib.auth.models import User, Group

from posts.models import Blog, Comentario, Post, Tag


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ["titulo", "introducao"]


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ["label"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["url", "autor", "titulo", "texto", "data", "tags", "comentarios"]


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ["post", "texto", "nome", "data"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
