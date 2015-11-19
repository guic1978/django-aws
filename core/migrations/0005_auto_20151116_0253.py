# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20151012_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('modelo', models.CharField(max_length=20)),
                ('operacao', models.CharField(max_length=1, choices=[(b'S', b'SALVAR'), (b'D', b'DELETAR'), (b'A', b'ALTERAR')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='pai',
        ),
        migrations.RemoveField(
            model_name='estoque',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='foto',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='preco',
            name='produto',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='marca',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Estoque',
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
        migrations.DeleteModel(
            name='Marca',
        ),
        migrations.DeleteModel(
            name='Preco',
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
