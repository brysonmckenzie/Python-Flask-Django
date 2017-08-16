# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    


    
    return render(request, 'ninja_app/index.html')

def ninjas(request):


    return render(request, 'ninja_app/ninja.html')



def show(request, id):
    
    context = {
        'color': id,
        }

    return render(request, 'ninja_app/show.html', context)