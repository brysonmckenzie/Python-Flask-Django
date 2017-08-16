# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# from User import User
from ..wall_app.models import *

print "hello!", User.objects.all()[0].id

#view pages

def login(request):
    
    return render(request, 'login_app/login.html')

def register(request):
    
    return render(request, 'login_app/register.html')

#post processing pages

def register_process(request):
    
    server_firstName = request.POST['html_firstName']
    server_lastName = request.POST['html_lastName']
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']

    if request.POST:
        if server_password == request.POST['html_passconf']:
            u = User.objects.create(first_name = server_firstName, last_name = server_lastName, email = server_email, password = server_password)
            print "**********New User Added**************"
            print u 

        return redirect('/login')

    return redirect('register')

def login_process(request):
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']

    user = User.objects.get(email = server_email)
    
    if request.POST:
        if user.password == server_password:
                request.session['user_id'] = user.id
        
        return redirect('/')
    return redirect('/login')

