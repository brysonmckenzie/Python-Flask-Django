# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcome_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='username_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
