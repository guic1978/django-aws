# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='especificacao',
            field=models.TextField(null=True, verbose_name=b'Especifica\xc3\xa7\xc3\xb5es', blank=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='produto',
            name='tags',
            field=models.ManyToManyField(to='core.Tag', blank=True),
        ),
    ]
