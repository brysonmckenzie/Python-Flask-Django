# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

import random

VALUES = ['Item #1', 'Item #2', 'Item #3', 'Item #4', 'Item #5', 'Item #6']

count = (len(VALUES))

def index(request):
    
    context = {'count': int(len(VALUES))}
    
    return render(request, 'suprise_app/index.html', context)




def suprise(request):
    
    
    
    random.shuffle(VALUES)
    suprises = []
    for x in range(int(request.POST['number'])):
        try:
            suprises.append(VALUES[x])
            context = { 
                'suprises': suprises, 
                'count': count,
                }
            print context
        except: 
            
            return redirect('/')
    return render(request, 'suprise_app/suprise.html', context)
    




        

        
