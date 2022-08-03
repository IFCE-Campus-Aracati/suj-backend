from django.urls import path, include

from rest_framework import routers

from posts.views import PostViewSet, UserViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"users", UserViewSet)
router.register(r"groups", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
