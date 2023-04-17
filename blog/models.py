"""Modelos do blog."""
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Create your models here.
class Categoria(models.Model):
    """Categoria de postagens."""

    descricao = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.descricao)


class Tag(models.Model):
    """Tags de postagens."""

    label = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.label)


class Post(models.Model):
    """Postagem do blog."""

    titulo = models.CharField(max_length=128, unique=True)
    conteudo = models.CharField(max_length=5000)
    pub_date = models.DateTimeField(default=timezone.now)

    autor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="postagens"
    )

    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name="postagens")

    visualizacoes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'Postagem: "{self.titulo}" de {self.autor} em {self.pub_date}'


class Comentario(models.Model):
    """Comentários em posts."""

    autor = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="comentarios"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")

    com_date = models.DateTimeField(default=timezone.now)

    texto = models.TextField()

    def __str__(self) -> str:
        return f"Comentário de {self.autor} em {self.com_date}"
