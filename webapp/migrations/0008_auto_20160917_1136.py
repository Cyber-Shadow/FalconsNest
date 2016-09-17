# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20160917_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='favemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('favorite', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='menumodel',
            name='category',
            field=models.CharField(choices=[('u', 'Unorderable'), ('sn', 'Snacks'), ('d', 'Drinks'), ('s', 'Sweets and Desserts'), ('i', 'Icecreams and Iceblocks')], max_length=14),
        ),
    ]
