# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render
from  models import *


def index(request):
    
    
    return render(request,'login/index.html')

def login_process(request):
    
    if request.method == 'POST':

        server_user_name = request.POST['name']
        server_password = request.POST['password']


        user = User.objects.get(name = server_user_name)
        
        if user.password == server_password:
            request.session['user_id'] = user.id
            return redirect('/wall')
    return redirect('/')
def register(request):
    
        
    return render(request,'login/register.html')

def register_process(request):
    if request.method == 'POST':
        server_first_name = request.POST['first_name']
        server_last_name = request.POST['last_name']
        server_user_name = request.POST['user_name']
        server_password = request.POST['password']

        if server_password == request.POST["password_confirmation"]:
            user = User.objects.create(first_name = server_first_name, last_name = server_last_name, user_name = server_user_name, password = server_password)
            request.session['user_id'] = user.id
            return redirect('/')


def wall(request):
    
    context ={
    'post': Post.objects.all()
            }
    
    message = Post.objects.all()
    print Post.message
   
    return render(request, 'login/wall.html',context)


def wall_process(request):
    
    if request.method == 'POST':
        server_message = request.POST['message']
        user = User.objects.get(id=request.session['user_id'])
        Post.objects.create(message = server_message, user = user)
        return redirect('/wall')

def dashboard_quotes(request):
    
    context ={
    'Quotes': Quote.objects.all()
            }
    
    message = Quotes.objects.all()
    
    return render(request, 'login/wall.html',context)



    


    if request.method == "POST":
        server_quote = request.POST['html_quotes'] 
        user = Quotes.objects.create(quotes = server_quote)



        # user = User.objects.get(email=request.session['email'])
        # book = Book.objects.get(id=id)
        # print type(book)
        # rating = int(request.POST['stars'])
        # Quotes.objects.create(review=request.POST['review'], rating=rating, book=book,user=user)

    return redirect(/dashboard)



def logout(request):
    
    if request.method == 'POST':
        request.session.clear() 

    return redirect('/')

   




    

    
