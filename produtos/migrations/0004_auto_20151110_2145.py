# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import produtos.models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_auto_20151105_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='download',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/guilhermereis/PycharmProjects/encontreaqui/core/protegido'), null=True, upload_to=produtos.models.local_download),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Alterado'),
        ),
        migrations.AlterField(
            model_name='categoriaimagem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em'),
        ),
        migrations.AlterField(
            model_name='categoriaimagem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Alterado'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Alterado'),
        ),
        migrations.AlterField(
            model_name='produtoimagem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em'),
        ),
        migrations.AlterField(
            model_name='produtoimagem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name=b'Alterado'),
        ),
    ]
