from rest_framework.serializers import ModelSerializer
from apps.core.models import PontoTuristico 
from apps.atracao.api.serializers import AtracaoSerializer 
from apps.endereco.api.serializers import EnderecoSerializer
from apps.avaliacao.api.serializers import AvaliacaoSerializer
from apps.comentario.api.serializers import ComentarioSerializer
from rest_framework.fields import SerializerMethodField

# Normalmente os endpoints possuem dois
# metodos para sua representacao, onde um
# traz informacoes detalhadas com outros
# relacionamentos(fks e etc.) e a principal que obtem
# apenas as informacoes principais
class PontoTuristicoSerializer(ModelSerializer):
    
    # Nested serializers
    atracao = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    avaliacao = AvaliacaoSerializer(many=True)
    comentario = ComentarioSerializer(many=True)

    # Caso exista algum campo extra
    descricao_completa = SerializerMethodField()
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto',
        'atracao', 'comentario', 'avaliacao', 'endereco',
        'descricao_completa']

    # Tambem e possivel criar o metodo no model
    # e chamar no serializer.
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)