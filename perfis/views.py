from django.shortcuts import render, HttpResponseRedirect, HttpResponse, Http404
from django.template.defaultfilters import slugify
from django.forms import modelformset_factory
from django.conf import settings

from .models import UsuarioCompra

def library(request):
    produtos = request.user.usuariocompra.produtos.all()
    if request.user.is_authenticated():
        return render(request, "perfis/library.html", locals())
    else:
        raise Http404