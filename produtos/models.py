# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db.models import signals
from django.dispatch.dispatcher import receiver
from django.core.urlresolvers import reverse

local_protegido = settings.UPLOADS_PROTEGIDOS

def local_download(instance, filename):
    if instance.usuario.username:
        return "%s/download/%s" %(instance.usuario.username, filename)
    else:
        return "%s/download/%s" %("default", filename)

class Produto(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True, verbose_name="Descrição")
    download = models.FileField(upload_to=local_download, storage=FileSystemStorage(location=local_protegido), null=True, blank=True)
    descricao_curta = models.TextField(null=True, blank=True, verbose_name="Descrição Curta")
    especificacao = models.TextField(null=True, blank=True, verbose_name="Especificações")
    sku = models.IntegerField(null=True, blank=True)
    order = models.IntegerField(default=0)
    ativo = models.BooleanField(default=False)
    preco = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    preco_desconto = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    class Meta:
        ordering = ['-order']

    def __unicode__(self):
    	return self.nome

    def preco_venda(self):
        if self.preco_desconto > 0:
            return self.preco_desconto
        else:
            return self.preco

    def imagem_principal(self):
        imagemPrincipal = ProdutoImagem.objects.filter(produto = self.id)[:1].get()
        return imagemPrincipal

    def get_absolute_url(self):
        return reverse('produtos.views.produto', args=[self.id])

class ProdutoImagem(models.Model):
    produto = models.ForeignKey(Produto)
    imagem = models.ImageField(upload_to="produtos/image/")
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

class Tag(models.Model):
    produto = models.ForeignKey(Produto)
    nome = models.CharField(max_length=50)
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.nome

class Categoria(models.Model):
    produto = models.ManyToManyField(Produto)
    nome = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField()
    ativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    # @property
    # def filhas(self):
    # 	return Categoria.objects.all().filter(pai = self.id)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos.views.categoria', args=[self.slug])

class CategoriaImagem(models.Model):
    categoria = models.ForeignKey(Categoria, null=True)
    imagem = models.ImageField(upload_to="produtos/image/")
    titulo = models.CharField(max_length=120, null=True, blank=True)
    imagem_principal = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Alterado")

    def __unicode__(self):
        return self.titulo

# @receiver(signals.post_save, sender=Produto)
# def atualizar_historico_save(sender, instance, **kwargs):
#     historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="S")
#     historico.save()
#
# @receiver(signals.post_delete, sender=Produto)
# def atualizar_historico_delete(sender, instance, **kwargs):
#     historico = Historico(usuario=instance.carrinho.user, modelo="carrinho", operacao="D")
#     historico.save()