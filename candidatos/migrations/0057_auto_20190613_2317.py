# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-06-13 23:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0056_auto_20190610_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudios_otros',
            name='comprobante',
            field=models.ImageField(blank=True, null=True, upload_to='compro_est_otros/'),
        ),
        migrations.AddField(
            model_name='estudios_pro',
            name='comprobante',
            field=models.ImageField(blank=True, null=True, upload_to='compro_est_pro/'),
        ),
    ]
