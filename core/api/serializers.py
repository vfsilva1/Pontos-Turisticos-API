from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from core.models import PontoTuristico
from atracoes.api.serializers import AtracoesSerializer
from enderecos.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer


class PontoTuristicoSerializer(serializers.ModelSerializer):
    Atracoes = AtracoesSerializer(many=True)
    Enderecos = EnderecoSerializer()

    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id', 'Nome', 'Descricao', 'Aprovado', 'Foto',
                  'Atracoes', 'Comentarios', 'Avaliacoes', 'Enderecos',
                  'descricao_completa', 'descricao_completa2']

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.Nome, obj.Descricao)
