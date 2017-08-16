# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime 

class User(models.Model):
    user_name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    birthday = models.DateField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Quotes(models.Model):
    quotes = models.TextField(max_length=1000)
    fav_quotes = models.TextField(max_length=1000)
    user = models.ForeignKey(User)

