from django.contrib import admin

from .models import UsuarioCompra

class UsuarioCompraAdmin(admin.ModelAdmin):
    class Meta:
        model = UsuarioCompra

admin.site.register(UsuarioCompra, UsuarioCompraAdmin)