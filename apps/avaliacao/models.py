from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    comentario = models.TextField(blank=True, null=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.comentario + ' - ' + self.user.username