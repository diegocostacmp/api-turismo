from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField

from apps.atracao.api.serializers import AtracaoSerializer 
from apps.endereco.api.serializers import EnderecoSerializer
from apps.avaliacao.api.serializers import AvaliacaoSerializer
from apps.comentario.api.serializers import ComentarioSerializer

from apps.core.models import PontoTuristico, DocIdentificacao
from apps.endereco.models import Endereco
from apps.atracao.models import Atracao
from apps.comentario.models import Comentario
from apps.avaliacao.models import Avaliacao


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

# Normalmente os endpoints possuem dois
# metodos para sua representacao, onde um
# traz informacoes detalhadas com outros
# relacionamentos(fks e etc.) e a principal que obtem
# apenas as informacoes principais
class PontoTuristicoSerializer(ModelSerializer):
    
    # Nested serializers
    atracao = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer(many=False)
    doc_identificacao = DocIdentificacaoSerializer(many=False)
    avaliacao = AvaliacaoSerializer(many=True)
    comentario = ComentarioSerializer(many=True)

    # Caso exista algum campo extra
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'aprovado', 'foto',
        'atracao', 'comentario', 'avaliacao', 'endereco',
        'descricao_completa', 'doc_identificacao']

        # read_only_fields = ['avaliacao', 'comentario']

    
    def cria_atracao(self, atracoes, ponto):
        for atracao in atracoes:
            print(atracao)
            at = Atracao.objects.create(**atracao)
            ponto.atracao.add(at)

    def cria_comentario(self, comentarios, ponto):
        for comentario in comentarios:
            print(comentario)
            coment = Comentario.objects.create(**comentario)
            ponto.comentario.add(coment)

    def cria_avaliacao(self, avaliacoes, ponto):
        for avaliacao in avaliacoes:
            print(avaliacao)
            av = Avaliacao.objects.create(**avaliacao)
            ponto.avaliacao.add(av)

    def create(self, validated_data):
        # ManytoMany atracao
        atracoes = validated_data['atracao']
        del validated_data['atracao']

        # ManyToMany comentario
        comentarios  = validated_data['comentario']
        del validated_data['comentario']

        # ManyToMany avaliacoes
        avaliacoes = validated_data['avaliacao'] 
        del validated_data['avaliacao']

        # Foreignkey
        endereco = validated_data['endereco']
        del validated_data['endereco']

        # OnetoOneField
        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']

        doci = DocIdentificacao.objects.create(**doc)
        ponto = PontoTuristico.objects.create(**validated_data)
        
        # Grava nested relacionados
        self.cria_atracao(atracoes, ponto)
        self.cria_comentario(comentarios, ponto)
        self.cria_avaliacao(avaliacoes, ponto)

        # Adicionando endereco
        end = Endereco.objects.create(**endereco)
        ponto.endereco = end 
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    # Tambem e possivel criar o metodo no model
    # e chamar no serializer.
    
    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)