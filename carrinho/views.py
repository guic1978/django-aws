# -*- encoding: utf-8 -*-
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import Carrinho, ItemCarrinho
from produtos.models import Produto
from django.template import loader, Context, RequestContext

def checa_carrinho(request):
    #Verifica se há carrinho aberto na sessão
    try:
        carrinho_id = request.session["CARRINHO_ID"]
    except:
        carrinho_id = False

    if carrinho_id:
        carrinho = Carrinho.objects.get(id=carrinho_id)
    else:
        carrinho=False

    return carrinho


def carrinho(request):
    #Verifica se há carrinho aberto na sessão
    carrinho = checa_carrinho(request)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)

    if len(itens) > 0:
        existe = True
    else:
        existe = False

    return render(request, "carrinho/mostra_carrinho.html", locals())


def alterar_carrinho(request, produto_id):
    #Verifica se o produto existe
    try:
        produto = Produto.objects.get(pk=produto_id)
    except:
        produto = False

    #Verifica se há carrinho aberto na sessão
    try:
        carrinho_id = request.session["CARRINHO_ID"]
    except:
        carrinho_id = False

    #Verifica se caso tenha encontrado carrinho aberto na sessão, obtem o carrinho do banco, se não cria um novo carro e guarda o id na sessão
    try:
        carrinho = Carrinho.objects.get(pk=carrinho_id)
    except Carrinho.DoesNotExist:
        carrinho = Carrinho()
        carrinho.user = request.user
        carrinho.save()
        request.session["CARRINHO_ID"] = carrinho.id

    if produto:
        #Cria ou obtem um produto no carrinho
        novo_item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
        if created:
            novo_item.carrinho = carrinho
            novo_item.save()
            messages.success(request, 'Item adicionado ao carrinho')

        else:
            novo_item.delete()
            messages.success(request, 'Item removido do carrinho')

        return HttpResponseRedirect(reverse('carrinho'))