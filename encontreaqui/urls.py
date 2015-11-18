"""encontreaqui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "produtos.views.produtos"),
    url(r'^produtos/', "produtos.views.produtos", name="produtos"),
    url(r'^busca/', "produtos.views.buscar", name="busca_produtos"),
    url(r'^produto/([0-9]+)/$', "produtos.views.produto", name="item_produto"),
    url(r'^produto/([0-9]+)/editar/', "produtos.views.editar_produto", name="editar_produto"),
    url(r'^produto/incluir/', "produtos.views.incluir_produto", name="incluir_produto"),
    url(r'^produto/([0-9]+)/imagens/', "produtos.views.gerenciar_imagem_produto", name="editar_imagem"),
    url(r'^produto/(?P<produto_id>.*)/download/(?P<filename>.*)$', "produtos.views.download_produto", name="download_produto"),
    url(r'^categoria/(?P<slug>.*)/$', "produtos.views.categoria", name="categoria"),
    url(r'^lib/', "perfis.views.library", name="library"),
    url(r'^carrinho/alterar/(?P<produto_id>.*)', "carrinho.views.alterar_carrinho", name="alterar_carrinho"),
    url(r'^carrinho/', "carrinho.views.carrinho", name="carrinho"),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
]


