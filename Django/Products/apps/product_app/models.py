# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Products(models.Model):
    product_name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    weight = models.IntegerField(default=10)
    price = models.IntegerField(default=10)
    cost = models.IntegerField(default=10n)
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
