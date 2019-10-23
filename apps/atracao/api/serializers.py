from rest_framework.serializers import ModelSerializer
from apps.atracao.models import Atracao 

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'nome', 'horario_func', 'idade_minima', 'foto']