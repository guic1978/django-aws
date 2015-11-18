from django.db import models
from django.contrib.auth.models import User

from produtos.models import Produto

class UsuarioCompra(models.Model):
    usuario = models.OneToOneField(User)
    produtos = models.ManyToManyField(Produto)

    def __unicode__(self):
        return self.usuario.username
