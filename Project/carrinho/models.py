# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from produtos.models import Produto
from core.models import Historico
from django.db.models import signals
from django.dispatch.dispatcher import receiver

class Carrinho(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    total = models.DecimalField(max_digits=50, default=0, decimal_places=2)
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return "%s %s" %(self.id, self.total)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho)
    produto = models.ForeignKey(Produto)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return "%s" %(self.produto.nome)

@receiver([signals.post_save, signals.post_delete], sender=ItemCarrinho)
def atualizar_total_carrinho(sender, instance, **kwargs):
    carrinho = instance.carrinho
    totals = [item.produto.preco_venda() for item in carrinho.itemcarrinho_set.all()]
    carrinho.total = sum(totals)
    carrinho.save()

@receiver(signals.post_save, sender=ItemCarrinho)
def atualizar_historico_save(sender, instance, **kwargs):
    historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="S")
    historico.save()

@receiver(signals.post_delete, sender=ItemCarrinho)
def atualizar_historico_delete(sender, instance, **kwargs):
    historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="D")
    historico.save()

