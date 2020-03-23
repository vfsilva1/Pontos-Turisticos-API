from django.contrib.auth.models import User
from django.db import models

class Avaliacao(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Comentario = models.TextField(null=True, blank=True)
    Nota = models.DecimalField(max_digits=3, decimal_places=1)
    Data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Usuario.username
