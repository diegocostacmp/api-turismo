from rest_framework.viewsets import ModelViewSet
from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class PontoTuristicoViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # model = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer

    

    # filtro personalizado, que pode contem
    # multiplos queryset
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)
    
    # Sobreescrevendo o metodo GET
    # de listagem

    # Retorna a lista completa
    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    # Cria um novo elemento
    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    # Exclui item especifico
    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)
    
    # Retorna um recurso especifico 
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    # Retorna o recurso a ser atualizado "put"
    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    # Atualiza especificamente um registro "patch"   
    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    # # Criando actions personalizadas
    # @action(method=['get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass

    