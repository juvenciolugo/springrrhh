# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-06 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0045_auto_20190603_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='tel',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Teléfono'),
        ),
    ]
