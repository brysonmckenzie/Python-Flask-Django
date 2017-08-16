# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from django.core import serializers

from models import User

def index(request):

    return render(request, 'welcome_app/index.html')


def login_process(request):

    if request.method == 'POST':
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
        server_alias = request.POST['html_alias']
        user = User.objects.get(email = server_email, alias = server_alias , password = server_password)

        if user.password == server_password:
            request.session['user_id'] = user.id
            request.session['alias'] = user.alias
           
            
        return redirect('/home')
           
    




def registration_process(request):
    
    if request.method == 'POST':
        server_name = request.POST['html_name']
        server_alias = request.POST['html_alias']
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']

        if server_password == request.POST['pass_conf']:
            user = User.objects.create(user_name = server_name, alias = server_alias, email = server_email, password = server_password)
            request.session['user_id'] = user.id
            request.session['alias'] = user.alias
            
    
        return redirect('/')


def home(request):
    
    context = {
        "user":User.objects.all()
        }

  
        
    return render(request, "welcome_app/home.html", context)

def logout(request):
    
    request.session.clear()
    if request.method == 'POST':
        
        request.session.clear()
            
        return redirect('/')

           


