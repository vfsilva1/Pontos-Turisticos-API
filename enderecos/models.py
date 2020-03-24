from django.db import models

class Endereco(models.Model):
    Linha1 = models.CharField(max_length=150)
    Linha2 = models.CharField(max_length=150, null=True, blank=True)
    Cidade = models.CharField(max_length=150)
    Estado = models.CharField(max_length=50, default="SP")
    Pais = models.CharField(max_length=70)
    Latitude = models.IntegerField(null=True, blank=True)
    Longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Linha1
