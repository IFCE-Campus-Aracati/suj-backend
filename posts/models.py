"""Modelos do blog."""
from django.db import models


# Create your models here.
class Tag(models.Model):
    """Uma tag de assunto de postagem."""

    label = models.CharField(max_length=30, unique=True)

    class Meta:
        """Meta config das tags."""

        ordering = ["label"]

    def __str__(self) -> str:
        return str(self.label)


class Post(models.Model):
    """Uma postagem no blog."""

    titulo = models.CharField(max_length=144, unique=True)
    texto = models.CharField(max_length=5000)
    data = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)

    class Meta:
        """Metaconfig de postagem."""

        ordering = ["data"]

    def __str__(self) -> str:
        return str(self.titulo)


class Comentario(models.Model):
    """Comentário no blog."""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comentarios"
    )

    texto = models.CharField(max_length=144)
    nome = models.CharField(max_length=20, default="anônimo")
    data = models.DateTimeField(auto_now_add=True)
