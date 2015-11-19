# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuariocompra',
            old_name='produto',
            new_name='produtos',
        ),
    ]
