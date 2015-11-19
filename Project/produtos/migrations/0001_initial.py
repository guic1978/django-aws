# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255, null=True, blank=True)),
                ('slug', models.SlugField()),
                ('ativo', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaImagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagem', models.ImageField(upload_to=b'produtos/image/')),
                ('titulo', models.CharField(max_length=120, null=True, blank=True)),
                ('imagem_principal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(to='produtos.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('descricao_curta', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o Curta', blank=True)),
                ('especificacao', models.TextField(null=True, verbose_name=b'Especifica\xc3\xa7\xc3\xb5es', blank=True)),
                ('sku', models.IntegerField(null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('ativo', models.BooleanField(default=False)),
                ('preco', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('preco_desconto', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-order'],
            },
        ),
        migrations.CreateModel(
            name='ProdutoImagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagem', models.ImageField(upload_to=b'produtos/image/')),
                ('titulo', models.CharField(max_length=120, null=True, blank=True)),
                ('imagem_principal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(to='produtos.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('produto', models.ForeignKey(to='produtos.Produto')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto'),
        ),
    ]
