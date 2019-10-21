from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField(max_length=150)
    linha2 = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=150)
    estado = models.CharField(max_length=35)
    pais = models.CharField(max_length=75)

    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.linha1