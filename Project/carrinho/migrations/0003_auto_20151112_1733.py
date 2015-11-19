# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_auto_20151112_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcarrinho',
            name='produto',
            field=models.ForeignKey(to='produtos.Produto'),
        ),
    ]
