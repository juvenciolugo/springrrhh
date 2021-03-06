# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-03 00:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0011_auto_20190503_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='cel',
            field=models.CharField(max_length=16, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='conyuge_tel',
            field=models.CharField(max_length=16, verbose_name='Teléfono o celular del conyuge'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='madre_tel',
            field=models.CharField(max_length=16, verbose_name='Teléfono o celular de la madre'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='empresa_tel',
            field=models.CharField(max_length=16, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='hermano_candidato',
            name='hermano_tel',
            field=models.CharField(max_length=16, verbose_name='Teléfono o celular del hermano'),
        ),
        migrations.AlterField(
            model_name='hijo_candidato',
            name='hijo_tel',
            field=models.CharField(max_length=16, verbose_name='Teléfono o celular del hijo'),
        ),
    ]
