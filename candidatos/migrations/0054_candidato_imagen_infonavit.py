# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-09 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0053_auto_20190607_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='imagen_infonavit',
            field=models.ImageField(blank=True, null=True, upload_to='infonavit/'),
        ),
    ]
