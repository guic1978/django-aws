# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255, null=True, blank=True)),
                ('ativo', models.BooleanField(default=True)),
                ('pai', models.ForeignKey(related_name='categoria_pai', blank=True, to='core.Categoria', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('principal', models.BooleanField(default=False)),
                ('arquivo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o', blank=True)),
                ('descricao_curta', models.TextField(null=True, verbose_name=b'Descri\xc3\xa7\xc3\xa3o Curta', blank=True)),
                ('sku', models.IntegerField(null=True, blank=True)),
                ('ativo', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('produto', models.OneToOneField(primary_key=True, serialize=False, to='core.Produto')),
                ('total', models.IntegerField(default=0)),
                ('minimo', models.IntegerField(null=True, blank=True)),
                ('vende_sem_estoque', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('produto', models.OneToOneField(primary_key=True, serialize=False, to='core.Produto')),
                ('original', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('desconto', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='categorias',
            field=models.ManyToManyField(to='core.Categoria', blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='marca',
            field=models.ForeignKey(blank=True, to='core.Marca', null=True),
        ),
        migrations.AddField(
            model_name='foto',
            name='produto',
            field=models.ForeignKey(to='core.Produto'),
        ),
    ]
