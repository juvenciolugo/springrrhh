# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-07 00:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0052_auto_20190606_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='tipo_baja',
            field=models.CharField(blank=True, max_length=9, null=True, verbose_name='Tipo de baja'),
        ),
    ]
