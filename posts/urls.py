from django.urls import path, include

from rest_framework import routers

from posts.views import (
    BlogViewSet,
    ComentarioViewSet,
    PostViewSet,
    TagViewSet,
    UserViewSet,
    GroupViewSet,
)

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"tags", TagViewSet)
router.register(r"blog", BlogViewSet)
router.register(r"comentarios", ComentarioViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
