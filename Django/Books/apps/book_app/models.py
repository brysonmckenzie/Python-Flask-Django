# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Books(models.Model):
    title = CharField(max_length=50)
    author = CharField(max_length=50)
    published date = DateTimeField(auto_now_added=False)
    category = CharField(max_length=50)
