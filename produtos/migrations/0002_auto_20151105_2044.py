# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriaimagem',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoriaimagem',
            name='categoria',
            field=models.ManyToManyField(to='produtos.Categoria'),
        ),
    ]
