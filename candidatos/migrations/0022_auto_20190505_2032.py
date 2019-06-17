# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-05 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0021_auto_20190505_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='rfc',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='RFC'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='vivienda_propia',
            field=models.CharField(max_length=8, null=True, verbose_name='Vive en casa'),
        ),
    ]
