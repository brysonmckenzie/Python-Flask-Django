# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random
import string 


def index(request):

    
    word = ''.join(random.choice(string.uppercase + string.digits) for i in range(14))
    context = {
    "word" : word
    }


    return render(request,'index.html', context)
    
def generator(request):
    
        c = string.digjits
        
        
        
        if 'counter' not in request.session.keys():
            request.session['counter'] = 0
        
        if request.method == 'POST':
             
            request.session['counter'] += 1
            
        

        return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')      
               
    
    
   
   
    

