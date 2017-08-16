# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from  .models import Products

def index(request):
    
    Products.objects.create(product_name = "iPhone", description = "test", weight = 10, price = "700", cost = "400", category = "cellphone")
    product = Products.objects.all()
    print(Products)
   

    return render(request, 'index.html')

