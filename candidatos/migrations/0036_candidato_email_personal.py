# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-05-20 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0035_auto_20190519_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='email_personal',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
