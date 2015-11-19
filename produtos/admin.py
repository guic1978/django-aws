# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Produto, Categoria, Tag, ProdutoImagem, CategoriaImagem

class CategoriaImagemInLine(admin.StackedInline):
    model = CategoriaImagem

class TagInLine(admin.StackedInline):
    prepopulated_fields = {"slug": ('nome',)}
    extra = 1
    model = Tag

class ImagemInLine(admin.StackedInline):
    extra = 2
    model = ProdutoImagem

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','sku','descricao_curta', 'preco', 'preco_desconto', 'ativo', 'categorias', 'link')
    inlines = [TagInLine, ImagemInLine]
    search_fields = ('nome', 'sku', 'categoria__nome')
    list_filter = ('preco', 'created_at')
    prepopulated_fields = {"slug": ('nome',)}
    readonly_fields = ['categorias', 'link']

    class Meta:
        model = Produto

    def categorias(self, obj):
        cat = []
        for i in obj.categoria_set.all():
            link = "<a href='/admin/produtos/categoria/" + str(i.id) + "'>" + i.nome +  "</a>"
            cat.append(link)
        return ", ".join(cat)

    categorias.allow_tags = True

    def link(self, obj):
        return "<a href='/produto/" + str(obj.id) + "'>Ver Produto</a>"

    link.allow_tags = True


admin.site.register(Produto, ProdutoAdmin)

class CategoriaAdmin(admin.ModelAdmin):
    # list_display = ('__unicode__','sku','descricao_curta', 'preco', 'preco_desconto', 'ativo')
    inlines = [CategoriaImagemInLine]
    prepopulated_fields = {"slug": ('nome',)}
    class Meta:
        model = Categoria

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag)
