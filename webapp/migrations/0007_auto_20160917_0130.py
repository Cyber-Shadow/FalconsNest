# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20160916_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='category',
            field=models.CharField(choices=[('u', 'Unorderable'), ('sn', 'Snacks'), ('d', 'Drinks'), ('s', 'Sweets and Deserts'), ('i', 'Icecreams and Iceblocks')], max_length=14),
        ),
    ]
