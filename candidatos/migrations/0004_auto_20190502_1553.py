# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-02 15:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0003_auto_20190502_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='calle',
            field=models.CharField(max_length=60, null=True, verbose_name='Calle'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='calle_dos',
            field=models.CharField(max_length=60, null=True, verbose_name='Y calle'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='calle_uno',
            field=models.CharField(max_length=60, null=True, verbose_name='Entre calle'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='cel',
            field=models.CharField(max_length=10, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='colonia',
            field=models.CharField(max_length=60, null=True, verbose_name='Colonia'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='cp',
            field=models.IntegerField(default=0, null=True, verbose_name='Código postal'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='esdo',
            field=models.CharField(max_length=60, null=True, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='fecha_nac',
            field=models.DateTimeField(null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='lugar_nac',
            field=models.CharField(max_length=60, null=True, verbose_name='Lugar de nacimiento'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='num_ext',
            field=models.CharField(max_length=5, null=True, verbose_name='Número exterior'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='pais_direc',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pais_de_direccion_cand', to='empleados.Country'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='trayectoria_de_casa',
            field=models.TimeField(null=True, verbose_name='Tiempo de trayectoria desde casa'),
        ),
    ]
