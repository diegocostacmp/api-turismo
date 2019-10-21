from django.db import models
from apps.atracao.models import Atracao
from apps.comentario.models import Comentario
from apps.avaliacao.models import Avaliacao
# Create your models here.
class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    
    def __str__(self):
        return self.nome
