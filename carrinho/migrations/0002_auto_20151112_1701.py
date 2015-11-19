# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemcarrinho',
            name='quantidade',
        ),
        migrations.AlterField(
            model_name='itemcarrinho',
            name='produto',
            field=models.OneToOneField(to='produtos.Produto'),
        ),
    ]
