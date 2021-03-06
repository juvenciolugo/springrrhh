# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-14 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0027_candidato_forma'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='especialidad_nombre',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre de la especialidad'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='postgrado_nombre',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre del postgrado'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='estado_salud',
            field=models.CharField(max_length=20, null=True, verbose_name='Estado de salud'),
        ),
    ]
