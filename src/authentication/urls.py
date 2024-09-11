"""Paths internos do app authentication."""

from django.urls import include, re_path

urlpatterns = [
    re_path("", include("djoser.urls")),
    re_path("", include("djoser.urls.jwt")),
]
