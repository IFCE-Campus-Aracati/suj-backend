"""Router do blog."""
from rest_framework import routers

from blog import views

router = routers.DefaultRouter()
router.register("posts", views.PostView)
