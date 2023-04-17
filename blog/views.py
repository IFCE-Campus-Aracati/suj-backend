"""Viewsets do blog."""
from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from blog import models, serializers


class PostView(viewsets.ModelViewSet):
    """Viewset de um Post."""

    queryset = models.Post.objects.all().order_by("-pub_date")
    serializer_class = serializers.PostSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_object(self):
        obj = super().get_object()
        obj.visualizacoes += 1
        obj.save()

        return obj


class UserViewSet(viewsets.ModelViewSet):
    """Viewset de user."""

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class CategoriaViewset(viewsets.ModelViewSet):
    """Viewset de categoria."""

    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class TagViewset(viewsets.ModelViewSet):
    """Viewset de tags."""

    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ComentarioViewset(viewsets.ModelViewSet):
    """Viewset de comentários."""

    basename = "comentarios"
    queryset = models.Comentario.objects.all().order_by("com_date")
    serializer_class = serializers.ComentarioSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
