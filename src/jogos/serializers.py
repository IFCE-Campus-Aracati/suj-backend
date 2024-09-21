from rest_framework import serializers
from .models import Equipes, Jogador, Modalidade  # Substitua pelo seu modelo correto

class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = '__all__'  # Inclui todos os campos do modelo, ou especifique os campos manualmente


class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipes
        fields = '__all__' 

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modalidade
        fields = '__all__' 