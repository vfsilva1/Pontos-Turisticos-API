from rest_framework.serializers import ModelSerializer
from enderecos.models import Endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'Linha1', 'Linha2', 'Cidade',
                  'Estado', 'Pais', 'Latitude', 'Longitude']