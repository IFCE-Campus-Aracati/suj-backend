"""Configurações de admin dos posts."""
from django import forms
from django.contrib import admin

from posts.models import Post, Tag


class PostForm(forms.ModelForm):
    """Formulário para postagem."""

    texto = forms.CharField(widget=forms.Textarea)

    class Meta:
        """Metaconfig do formulário."""

        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    """Admin para postagens."""

    form = PostForm


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
