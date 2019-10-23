from rest_framework.viewsets import ModelViewSet
from apps.atracao.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_fields = ('nome', 'horario_func')