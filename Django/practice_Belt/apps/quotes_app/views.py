# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

def index(request):
    


    return render(request, 'quotes_app/index.html')

def registration_process(request):
    
    if request.method == 'POST':
        server_firstname = request.POST['html_firstname']
        server_lastname = request.POST['html_lastname']
        server_alias = request.POST['html_alias']
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        server_birthday = request.POST['html_birthday']
        
        if server_password == request.POST['html_pass_conf']:
            user = User.objects.create(first_name = server_firstname, last_name = server_lastname, alias = server_alias, email = server_email, password = server_password, birthday = server_birthday)
            request.session['user_id'] = user.id


        return redirect('/')


def login_process(request):
    
    if request.method == 'POST':
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        
        user = User.objects.get(email = server_email)

        if user.password == server_password:
            request.session[user_id] = user.id 
        return redirect('/dashboard')
    return ('/')


def dashboard(request):

    user = User.objects.get(id=request.session['user_id'])
    
    context = {
        
        'users': User.objects.all()

    }

    message = User.objects.all()

    
   

    
    return render(request, 'quotes_app/dashboard.html', context)



def logout(request):
    
    if request.method == 'POST':
        
        request.session.clear()
    
    return redirect('/')