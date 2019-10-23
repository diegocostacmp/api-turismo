from django.db import models
from apps.atracao.models import Atracao
from apps.comentario.models import Comentario
from apps.avaliacao.models import Avaliacao
from apps.endereco.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacao = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    foto = models.ImageField(upload_to='ponto_turistico', blank=True, null=True)
    def __str__(self):
        return self.nome
