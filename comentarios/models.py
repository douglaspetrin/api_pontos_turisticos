from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario.first_name + ' - ' + self.comentario  # aqui tá pegando first_name do próprio AbstractUser Model
