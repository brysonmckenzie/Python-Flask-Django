# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from datetime import datetime

from ..book_app.models import *


def index(request):
    
    return render(request, 'login_app/login.html')


def register(request):
    
    return render(request, 'login_app/register.html')


def register_process(request):

    server_username = request.POST['html_username']
    server_alias = request.POST['html_alias']
    server_email = request.POST['html_email']
    server_password = request.POST['html_password']

    if request.method == 'POST':
        
        if server_password == request.POST['html_passconf']:
            
            User.objects.create(
                user_name = server_username,
                alias = server_alias,
                email = server_email,
                password = server_password,
            )
            
            print '**************** New User *********************'
        
        return redirect('/login')
    
    return redirect('/login')

def login_process(request):
    
    server_email = request.POST['html_email']
    user = User.objects.get(email = server_email)
    
    if request.method == 'POST':
        request.session['user_id'] = user.id
        print "********* User Logged IN **************"
        print "********" + str(user.id) + "****ID IN SESSIONS****" 
        print "The user #" + str(user.id) + "has now logged in the system" + str(datetime.now())
        return redirect('/')

def log_out(request):
    
    if request.method == 'POST':
        request.session.clear()

    return redirect('/login')