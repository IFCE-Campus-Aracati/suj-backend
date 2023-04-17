"""Router do blog."""
from rest_framework import routers

from blog import views

router = routers.DefaultRouter()
router.register("posts", views.PostView)
router.register("users", views.UserViewSet)
router.register("categorias", views.CategoriaViewset)
router.register("tags", views.TagViewset)
router.register("comentarios", views.ComentarioViewset)
