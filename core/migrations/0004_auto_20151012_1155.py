# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151012_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='tag',
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(blank=True, to='core.Categoria', null=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tags',
            field=models.ManyToManyField(to='core.Tag', blank=True),
        ),
    ]
