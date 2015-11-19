from django.forms import ModelForm
from .models import Produto, ProdutoImagem

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'
        exclude = ('usuario', 'order', 'slug')

class ProdutoImagemForm(ModelForm):
    class Meta:
        model = ProdutoImagem
        fields = ['imagem','imagem_principal']