# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-03 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0010_auto_20190503_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='padre_tel',
            field=models.CharField(max_length=16, null=True, verbose_name='Teléfono o celular del padre'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='tel',
            field=models.CharField(max_length=16, null=True, verbose_name='Teléfono'),
        ),
    ]
