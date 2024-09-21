from django.db import models

from authentication.models import User

CATEGORIA_CHOICES = [
    ('M','Masculino'),
    ('F','Feminino'),
    ('MT','Misto')
]

TIPO_CHOICES = [
    ('I','Individual'),
    ('C','Coletivo')
]


# Create your models here.
class Modalidade(models.Model):
    nome = models.CharField(name="nome", max_length=20)
    tipo = models.CharField(choices = TIPO_CHOICES, max_length=1,default = 'I')
    categoria = models.CharField(choices=CATEGORIA_CHOICES,max_length=2, default='MT')
    min_jogadores = models.IntegerField(default=1)




class Equipes(models.Model):
    
    modalidade = models.ForeignKey(Modalidade,on_delete=models.CASCADE)
    nome = models.CharField(name="nome", max_length=25, null=False,unique=True,)
    
   

class Jogador(models.Model):
   nome = models.CharField(max_length=20)
   equipes = models.ManyToManyField(Equipes, through='Jogadores_em_equipes')



class Jogadores_em_equipes(models.Model):
    jogador = models.ForeignKey(Jogador,on_delete=models.CASCADE)
    equipe = models.ForeignKey(Equipes, to_field="nome",on_delete=models.CASCADE)