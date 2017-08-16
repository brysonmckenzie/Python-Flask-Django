# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    
    if 'first_name' not in session.keys()
    
        request.session['first_name'] = ""



        request.session['last_name'] = ""
        request.session['location'] = ""
        request.session['language'] = ""
        request.session['comnment'] = ""
    
   



        return render(request, 'index.html')



def process(request):
    
    if request.method == 'POST':

        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        
    

        return redirect('/results')


    
def results(request):
    
   
    context = {
        'first_name': request.session['first_name'],
        'last_name': request.session['last_name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
    }


    return render(request, 'results.html', context)


