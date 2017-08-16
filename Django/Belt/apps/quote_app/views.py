# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from datetime import datetime

from models import Quotes, User

def index(request):
    
    
    
    
    return render(request,'quote_app/index.html')







def registration_process(request):
    

    if request.method == 'POST':
        server_user_name = request.POST['html_user_name']
        server_name_alias = request.POST['html_alias']
        server_email = request.POST['html_email']
        server_password = request.POST['html_pass_conf']
        server_birthday = request.POST['html_birthday']

    if server_password == request.POST["html_pass_conf"]:
            
            user = User.objects.create(user_name = server_user_name, alias = server_name_alias, email = server_email, password = server_password, birthday = server_birthday)
            request.session['user_id'] = user.id
            
            
            return redirect('/dashboard')

    return redirect('/')






def login_process(request):
    

        server_user_name = request.POST['user_name']
        server_password = request.POST['password']


        user = User.objects.get( user_name = server_user_name)
        
        if user.password == server_password:
            request.session['user_id'] = user.id
            return redirect('quote_app/dashboard')


        return redirect('/')


def dashboard(request):

    context ={
    'quote': Quotes.objects.all()
            }
    message = Quotes.objects.all()

    return render(request, 'quote_app/dashboard.html')


def create_q(request):
    
    
    if request.method == 'POST':
        server_quotes = request.POST["html_quotes"]
        Quotes.objects.create(quotes = server_quotes, user = user) 
        print request.POST
        print "$$$$$$$$$$$$$$$$$$$$$"


    
        return redirect('/dashboard')


def logout(request):
    
    if request.method == 'POST':
        request.session.clear() 

    return redirect('/')