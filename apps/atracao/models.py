from django.db import models

# Create your models here.
class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    foto = models.ImageField(upload_to='atracao', blank=True, null=True)
    

    def __str__(self):
        return self.nome