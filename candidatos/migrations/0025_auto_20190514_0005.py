# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-14 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0024_auto_20190509_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hijo_candidato',
            name='hijo_edad',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='Edad del hijo'),
        ),
    ]
