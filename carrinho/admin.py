# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Carrinho, ItemCarrinho

class ItemCarrinhoInLine(admin.TabularInline):
    model = ItemCarrinho

class CarrinhoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total')
    inlines = [ItemCarrinhoInLine]
    class Meta:
        model = Carrinho

admin.site.register(Carrinho, CarrinhoAdmin)