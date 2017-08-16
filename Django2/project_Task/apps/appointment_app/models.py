# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=38)
    last_name = models.CharField(max_length=38)
    email = models.CharField(max_length=38, unique=True)
    password = models.CharField(max_length=38)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    task = models.CharField(max_length=38)
    time = models.TimeField()
    date = models.DateField(blank=True, null=True)
    status = models.BooleanField()
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)