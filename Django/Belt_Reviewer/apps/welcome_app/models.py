# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=30)
    alias = models.CharField(max_length= 30)
    email = models.CharField(max_length= 30)
    password = models.CharField(max_length= 30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Books(models.Model):
    Authors = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    

class Reviews(models.Model):
    user_reviews = models.TextField(max_length=1000)
    books = models.ForeignKey(Books)
    ratings = models.CharField(max_length=30)
    user = models.ForeignKey(User)
