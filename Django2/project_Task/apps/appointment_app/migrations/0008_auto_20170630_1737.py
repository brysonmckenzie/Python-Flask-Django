# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_app', '0007_auto_20170630_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(),
        ),
    ]
