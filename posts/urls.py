from django.urls import include, path
from rest_framework import routers

from posts.views import ComentarioViewSet, PostViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"tags", TagViewSet)
router.register(r"comentarios", ComentarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
