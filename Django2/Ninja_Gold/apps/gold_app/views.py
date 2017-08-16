# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from random import randrange
from datetime import datetime

def index(request):
    
    if 'gold' not in request.session.keys():
            request.session['gold'] = 0
    
    if 'log' not in request.session.keys():
        request.session['log'] = []
    
    return render(request,'gold_app/index.html')    
    
    
def process_money(request):
    
    date = datetime.now()
    

    if request.method == 'POST':
         
        if request.POST['info'] == 'farm':
            gold_found = randrange(10,20)
            request.session['gold'] += gold_found
            string = "You have found " + str(gold_found) + " amount of gold!" 
            request.session['log'].append(string)
            print request.POST

        if request.POST['info'] == 'cave':
            gold_found = randrange(5,10)
            request.session['gold'] += gold_found
            string = "You have found " + str(gold_found) + " amount of gold!"
            request.session['log'].append(string)

        
        if request.POST['info'] == "house":
            gold_found = randrange(2,5)
            request.session['gold'] += gold_found
            string = "You have found " + str(gold_found) + " amount of gold!"
            print request.POST
            request.session['log'].append(string)
        
        if request.POST['info'] == 'casino':
            gold_found = randrange(-50,50)
            if gold_found > 0 :
                request.session['gold'] += gold_found
                string = "You have found " + str (gold_found) + " amount of gold!"
                request.session['log'].append(string)
                print request.POST
            else:
                request.session['gold'] -= gold_found
                string = "You lose " + str (gold_found) + " amount of gold!"
                request.session['log'].append(string)

    return redirect('/')

def clear(request):
    if request.method == 'POST':
        request.session.clear()

    return redirect('/')
                

            
            
    
        
            

        # log = request.session['log'] #variable log stores the array
        # log.append(string) #it's being pushed into array
        # # request.session['log'] = log


    