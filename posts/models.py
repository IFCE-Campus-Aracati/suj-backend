from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.TextField(max_length=144, unique=True)
    texto = models.TextField(max_length=5000)
    data = models.DateTimeField(auto_now_add=True)
