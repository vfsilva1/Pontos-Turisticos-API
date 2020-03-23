from collections import defaultdict

from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Endereco

class PontoTuristico(models.Model):
    Nome = models.CharField(max_length=150)
    Descricao = models.TextField()
    Aprovado = models.BooleanField(default=False)
    Atracoes = models.ManyToManyField(Atracao)
    Comentarios = models.ManyToManyField(Comentario)
    Avaliacoes = models.ManyToManyField(Avaliacao)
    Endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nome