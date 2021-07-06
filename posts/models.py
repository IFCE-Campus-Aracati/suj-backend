from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=5000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
