# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-06 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0047_auto_20190606_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiencia',
            name='empresa_fecha_separacion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de separación de la empresa'),
        ),
    ]
