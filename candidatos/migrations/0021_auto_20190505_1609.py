# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-05 16:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0020_auto_20190505_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiencia',
            old_name='experiencia',
            new_name='candidato',
        ),
        migrations.RenameField(
            model_name='referencia',
            old_name='referencia',
            new_name='candidato',
        ),
    ]
