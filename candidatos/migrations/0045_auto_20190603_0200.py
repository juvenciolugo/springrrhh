# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-03 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0044_cand_docs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cand_docs',
            name='Observaciones',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Observaciones'),
        ),
    ]
