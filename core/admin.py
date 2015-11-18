# # -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Historico
# from utils import CustomAdmin
# from .models import Produto, Marca, Categoria, Estoque, Preco, Foto, Tag
#
# class FotoInLine(admin.StackedInline):
# 	model = Foto
#
# class PrecoInLine(admin.StackedInline):
# 	model = Preco
#
# class EstoqueInLine(admin.StackedInline):
# 	model = Estoque
#
# class ProductAdmin(admin.ModelAdmin):
# 	inlines = [FotoInLine, PrecoInLine, EstoqueInLine]
# 	list_display = ('id', 'nome', 'sku', 'marca', 'ativo')
# 	list_filter = ['ativo']
# 	search_fields = ('nome', 'sku')
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'modelo', 'operacao', 'created_at')
    model = Historico

# admin.site.register(Marca)
# admin.site.register(Categoria)
# admin.site.register(Tag)
admin.site.register(Historico, HistoricoAdmin)
