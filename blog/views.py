"""Viewsets do blog."""

from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from blog import models, serializers


class PostView(viewsets.ModelViewSet):
    """Viewset de um Post."""

    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
