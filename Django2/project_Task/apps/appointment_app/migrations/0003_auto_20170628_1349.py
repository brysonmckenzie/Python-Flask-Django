# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0002_auto_20170628_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(max_length=38),
        ),
    ]
