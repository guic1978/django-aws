# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20151105_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='produto',
        ),
        migrations.AddField(
            model_name='categoria',
            name='produto',
            field=models.ManyToManyField(to='produtos.Produto'),
        ),
        migrations.RemoveField(
            model_name='categoriaimagem',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoriaimagem',
            name='categoria',
            field=models.ForeignKey(to='produtos.Categoria', null=True),
        ),
    ]
