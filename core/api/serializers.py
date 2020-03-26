from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from atracoes.models import Atracao
from core.models import PontoTuristico, DocIdentificacao
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecoSerializer
from enderecos.models import Endereco

class DocIdentificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = '__all__'

class PontoTuristicoSerializer(serializers.ModelSerializer):
    Atracoes = AtracoesSerializer(many=True)
    Enderecos = EnderecoSerializer()
    descricao_completa = SerializerMethodField()
    doc_identificacao = DocIdentificacaoSerializer()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'Nome', 'Descricao', 'Aprovado', 'Foto',
                  'Atracoes', 'Comentarios', 'Avaliacoes', 'Enderecos',
                  'descricao_completa', 'descricao_completa2', 'doc_identificacao']

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.Nome, obj.Descricao)

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['enderecos']
        del validated_data['enderecos']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.Enderecos = end

        doci = DocIdentificacao.objects.create(**doc)
        ponto.Doc_Identificacao = doci

        ponto.save()

        return ponto