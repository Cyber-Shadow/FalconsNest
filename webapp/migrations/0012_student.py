# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-19 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20160918_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.IntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
            ],
        ),
    ]
