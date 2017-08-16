# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
import string 


def index(request):
    

        
    if 'counter' not in request.session.keys():
        request.session['counter'] = 0

    
    
    word = ''.join(random.choice(string.uppercase + string.digits) for i in range(14))
    context = {
    "word" : word
    }


    return render(request,'word_app/index.html', context)
    
def generator(request):
        
        if request.method == 'POST':
            if 
            request.session['counter'] += 1
            
        

        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')      
               
    
    
   
   
    