# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-23 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0038_estudios_otros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='empresa_fecha_separacion',
            field=models.DateTimeField(null=True, verbose_name='Fecha de separación de la empresa'),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='separacion_motivo',
            field=models.CharField(max_length=100, null=True, verbose_name='¿Cuál fué el motivo de la separación?'),
        ),
        migrations.AlterField(
            model_name='hermano_candidato',
            name='hermano_apellido_materno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido materno del hermano'),
        ),
        migrations.AlterField(
            model_name='hermano_candidato',
            name='hermano_apellido_paterno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido paterno del hermano'),
        ),
        migrations.AlterField(
            model_name='hermano_candidato',
            name='hermano_nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre del hermano'),
        ),
        migrations.AlterField(
            model_name='hijo_candidato',
            name='hijo_apellido_materno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido materno del hijo'),
        ),
        migrations.AlterField(
            model_name='hijo_candidato',
            name='hijo_apellido_paterno',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellido paterno del hijo'),
        ),
        migrations.AlterField(
            model_name='hijo_candidato',
            name='hijo_nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre del hijo'),
        ),
        migrations.AlterField(
            model_name='referencia',
            name='referencia_domicilio',
            field=models.CharField(max_length=200, null=True, verbose_name='Domicilio de la referencia'),
        ),
        migrations.AlterField(
            model_name='referencia',
            name='referencia_tel',
            field=models.CharField(max_length=16, null=True, verbose_name='Teléfono'),
        ),
    ]
