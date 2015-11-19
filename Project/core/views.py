# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
# from core.models import Produto
# from core.models import Categoria

# def index(request):
#     # produtos = Produto.objects.all()
#     return render(request, "home.html")
#
# def produtos(request):
#     produtos = Produto.objects.all()
#     return render(request, "lista_produtos.html", {'produtos': produtos})
#
# def mostrar_produto(request, produto_id):
# 	try:
# 		produto = Produto.objects.get(pk=produto_id)
# 		categorias = Categoria.objects.all()
# 	except Produto.DoesNotExist:
# 		raise Http404("Produto não encontrado")
# 	else:
# 		return render(request, "mostra_produto.html", {'produto': produto, 'categorias': categorias})