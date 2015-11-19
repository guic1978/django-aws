# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

OPERACAO = (
    ("S", "SALVAR"),
    ("D", "DELETAR"),
    ("A", "ALTERAR"),
)

class Historico(models.Model):
    usuario = models.ForeignKey(User)
    modelo = models.CharField(max_length=20)
    operacao = models.CharField(max_length=1, choices=OPERACAO)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")

    def __unicode__(self):
		return u"Usuário: %s, Modelo: %s, Operação: %s" %(self.usuario, self.modelo, self.operacao)
