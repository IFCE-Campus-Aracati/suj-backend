from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogadorViewSet, EquipesViewSet, ModalidadeViewSet

# Crie um router para registrar as views
router = DefaultRouter()
router.register(r'jogadores', JogadorViewSet, basename="jogador")  # A rota jogadores/ lidará com o ViewSet
router.register(r'equipes',EquipesViewSet, basename="equipe")
router.register(r'modalidade',ModalidadeViewSet, basename="modalidae")


urlpatterns = [
    path('', include(router.urls)), 
      
]