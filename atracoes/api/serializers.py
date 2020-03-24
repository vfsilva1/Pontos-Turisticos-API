from rest_framework import serializers
from atracoes.models import Atracao

class AtracoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id', 'Nome', 'Descricao', 'HorarioFuncionamento', 'IdadeMinima', 'Foto']