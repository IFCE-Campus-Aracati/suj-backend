"""Paths raiz do site."""

import os

from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(os.getenv("ADMIN_PATH"), admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("auth/", include("authentication.urls")),
    path("api-jogos/", include("jogos.urls") )
]
