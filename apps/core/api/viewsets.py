from rest_framework.viewsets import ModelViewSet
from apps.core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
class PontoTuristicoViewSet(ModelViewSet):
    
    """
    API endpoint that allows users to be viewed or edited.
    """
    # model = PontoTuristico.objects.filter(aprovado=True)
    serializer_class = PontoTuristicoSerializer
    
    filter_backends = [SearchFilter]

    # Requer autenticacao do usuario
    # Caso o usuario necessite ser adm use: IsAdminUser
    # Para maior entendimento verifique os
    # metodos de autenticacao
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Requer que o usuario seja Admin


    # Como sera o usuario sera autenticado
    authentication_classes = [TokenAuthentication]

    # Campos para pesquisa na url, "?search=nome or descricao"
    search_fields = ('id','nome', 'descricao', 'endereco__linha1')
    
    # Este campo retorna apenas um objeto,
    # normalmente a pk do objeto
    lookup_field = 'aprovado'

    # filtro personalizado, que pode contem
    # multiplos queryset
    def get_queryset(self):

        # Filtro utilizando queryString na url
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        
        queryset = PontoTuristico.objects.all()
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset = queryset.filter(nome=nome)
        
        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)
        
        return queryset
    
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

    