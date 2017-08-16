# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

def index(request):

    return render(request, 'landscape_app/index.html')

def show(request, id):
    
    context = {
        'picture' : id
        
    }
    print "********"
    print context['picture']
    print "********"

    return render(request, 'landscape_app/show.html', context)