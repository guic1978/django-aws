# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151012_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='tags',
        ),
        migrations.AddField(
            model_name='produto',
            name='tag',
            field=models.ForeignKey(blank=True, to='core.Tag', null=True),
        ),
    ]
