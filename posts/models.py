from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    titulo = models.CharField(max_length=20)
    introducao = models.CharField(max_length=500)


class Tag(models.Model):
    label = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ["label"]

    def __str__(self) -> str:
        return self.label


class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=144, unique=True)
    texto = models.CharField(max_length=5000)
    data = models.DateTimeField(auto_now_add=True)

    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ["data"]

    def __str__(self) -> str:
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")

    texto = models.CharField(max_length=144)
    nome = models.CharField(max_length=20, default="anônimo")
    data = models.DateTimeField(auto_now_add=True)
