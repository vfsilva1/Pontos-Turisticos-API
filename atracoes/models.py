from django.db import models

class Atracao(models.Model):
    Nome = models.CharField(max_length=150)
    Descricao = models.TextField()
    HorarioFuncionamento = models.TextField()
    IdadeMinima = models.IntegerField()
    Foto = models.ImageField(upload_to='atracoes', null=True, blank=True)

    def __str__(self):
        return self.Nome
