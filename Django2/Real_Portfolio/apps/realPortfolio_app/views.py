# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    
    return render(request, 'index.html')


def about(request):
    
    return render(request,'about.html')


def test(request):
    
    return render(request, 'test.html')


def projects(request):
    
    return render(request, 'projects.html')
