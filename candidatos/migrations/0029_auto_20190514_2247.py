# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-14 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0028_auto_20190514_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='primaria_inicio',
            field=models.CharField(max_length=4, null=True, verbose_name='Fecha de inicio'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='primaria_termino',
            field=models.CharField(max_length=4, null=True, verbose_name='Fecha de término'),
        ),
    ]
