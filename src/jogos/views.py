from requests import Response
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Equipes, Jogador, Modalidade  # Substitua pelo seu modelo correto
from .serializers import JogadorSerializer, EquipeSerializer, ModalidadeSerializer
from rest_framework import status

class JogadorViewSet(viewsets.ModelViewSet):
    
    queryset = Jogador.objects.all()  # Defina o queryset para o modelo Jogador
    serializer_class = JogadorSerializer  # Defina o serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EquipesViewSet(viewsets.ModelViewSet):
    
    queryset = Equipes.objects.all()  # Defina o queryset para o modelo Jogador
    serializer_class = EquipeSerializer  # Defina o serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

class ModalidadeViewSet(viewsets.ModelViewSet):
    queryset = Modalidade.objects.all()  # Defina o queryset para o modelo Jogador
    serializer_class = ModalidadeSerializer  # Defina o serializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly] 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)