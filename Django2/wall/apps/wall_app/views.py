# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse

from models import User, Message, Comment

def index(request):
    print request.session['user_id']
    
    name =  User.objects.get(id = request.session['user_id'])

    context = {
        'user':User.objects.all(),
        'message': Message.objects.all().order_by('-created_at'),
        'comments':Comment.objects.all().order_by('-created_at'),
        'name':User.objects.get(id = request.session['user_id'])   
    }

    return render(request, 'wall_app/index.html', context)
    
def wall_message_create(request):
    
    


    if request.method == 'POST':
        
        user = request.session['user_id']

        message = request.POST['message']
        
        Message.objects.create(message = message, user_id = user)

        return redirect('/')

        
def wall_comment_create(request, id):
    
    
    if request.method == 'POST':
        
        user = User.objects.get(id = request.session['user_id'])

        c = Comment.objects.create(comment = request.POST['comment'], message_id = id, user_id = user.id )
        print c 
        return redirect('/')

def log_out(request):
    
    if request.method == 'POST':
        request.session.clear()

    return redirect('/login')
    


  


        

