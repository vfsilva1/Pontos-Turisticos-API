from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Comentario = models.TextField()
    Data = models.DateTimeField(auto_now_add=True)
    Aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.Usuario.username