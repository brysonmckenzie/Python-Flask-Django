# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User, Task
from datetime import datetime
from django.utils.timezone import localdate, now
from django.utils.timezone import localtime
from django.utils.timezone import datetime


from django.contrib import messages
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request): #mainpage

    if 'user_id' not in request.session:
        messages.error(request, 'Please login!')
        return redirect('/login')
        
    current_user = request.session['user_id']

    context = {
        'users':User.objects.all(),
        'tasks':Task.objects.filter(user_id = current_user),
        'user':User.objects.get(id = request.session['user_id']),
        'today':Task.objects.filter(date= localdate(now()), user_id = current_user),
        'date': localdate(now()),
    }

    return render(request,'appointment_app/index.html', context)

def login(request): 

    return render(request, 'appointment_app/login.html')


def register(request):  #registration page

    return render(request,'appointment_app/registration.html')

def show_update(request, id):
    
    if 'user_id' not in request.session:
        messages.error(request, 'Please login!')
        return redirect('/login')
    
    context = {
    'task':Task.objects.get(id = id),
    }

    return render(request,'appointment_app/update.html', context)

def add_task(request):
    
    if 'user_id' not in request.session:
        messages.error(request, 'Please login!')
        return redirect('/login')
    
    current_user = request.session['user_id']

    server_task = request.POST['html_task']
    server_date = request.POST['html_date']
    server_time = request.POST['html_time']
    server_status = False
    
    # isValid = True

    # if len(server_task) < 1:
    #     messages.error(request,'Invalid field length for task!')
    #     isValid = False
    # if len(server_time) < 1:
    #     messages.error(request,'Invalid field length for first name!')
    #     isValid = False
    # if server_date < localdate(now()):
    #     messages.error(request,'Enter a valid date!')
    #     isValid = False
    
    # if not isValid:
    #     return redirect("/")
    try:
        Task.objects.create(
            task = server_task,
            time = server_time,
            date = server_date, 
            status = server_status,
            user_id = current_user,
            )
        return redirect('/')
    except:
        messages.error(request,'Try Again!')
        return redirect('/')
                                
                                                        
def delete(request,id):
    
    Task.objects.get(id = id).delete()
    
    return redirect('/')

def update_process(request, id):
    
    server_task = request.POST['html_task']
    server_time = request.POST['html_time']
    server_date = request.POST['html_date']
    server_status = request.POST['html_status']
    
    task = Task.objects.get(id = id)
    task.task = server_task 
    task.status = server_status 
    task.date = server_date
    print task.date 
    task.time = server_time
    task.save()

    return redirect('/')


def register_process(request): #registration_process

    server_firstname = request.POST['html_firstname']
    server_lastname = request.POST['html_lastname']
    server_email = request.POST['html_email']
    server_birthday = request.POST['html_birthday']
    server_password = request.POST['html_password']

    encrypted_password = bcrypt.hashpw(server_password.encode('utf-8'), bcrypt.gensalt())

    print "******************"
    print encrypted_password
    print len(encrypted_password)
    print "******a***********"


    print request.POST,"<={****************{{{{{"

    isValid = True

    if len(server_firstname) < 1:
        messages.error(request,'Invalid field length for first name!')
        isValid = False

    if  server_firstname.isalpha() == False:
        messages.error(request,'You need to enter characters only for first name!')
        isValid = False

    if  len(server_lastname) < 1:
        messages.error(request,'Invalid field length for last name!')
        isValid = False

    if  server_lastname.isalpha() == False:
        messages.error(request,'You need to enter characters only for last name!')
        isValid = False

    if  len(server_email) < 1:
        messages.error(request,'Invalid field length for email!')
        isValid = False

    if not EMAIL_REGEX.match(server_email):
        messages.error(request,'Please enter a valid email address')
        isValid = False  
    
    if  server_birthday == '':
        messages.error(request,'Please enter a valid date!')
        isValid = False

    if server_password < 1:
        messages.error(request, 'Insert a password!')
        isValid = False

    if  server_password != request.POST['html_passconf']:
        messages.error(request, 'Passwords doesnt match')
        isValid = False
   
    if not isValid:
        
        redirect('/register')
        # print server_birthday

    # try:
        User.objects.create(
            first_name = server_firstname,
            last_name = server_lastname,
            email = server_email,
            password = encrypted_password,
            birthday = server_birthday,
        )
        print '****************New User*********************'
        messages.success(request, 'You have successfully created a profile!')
        return redirect('/login')
    except:
        messages.error(request, 'Invalid login!')
        return redirect('/register')

    



def login_process(request): 
        server_email = request.POST['html_email']
        server_password = request.POST['html_password']
       
        isValid = True

        if len(server_email) < 1:
            messages.error(request, 'Please enter an valid email!')
            isValid = False

        if len(server_password) < 1:
            messages.error(request, 'Enter a password!')
            isValid = False
        
        if len(server_password) > 8:
            messages.error(request, 'Password can not be greater than 8 charchaters!')
            isValid = False

        if not isValid:
            return redirect('/login')
       

        

        try:

            user = User.objects.get(email = server_email)

            if bcrypt.hashpw(server_password.encode(), user.password.encode()) != user.password:
                messages.error(request, 'Password is invalid!')
                return redirect('/login')
            else:
                
                request.session['user_id'] = user.id
                print "************************"
                print "User is now logged in"
                print "************************"
                print "ID # ",request.session['user_id']
                print "************************"
                return redirect('/')

        except:

            messages.error(request, 'Invalid email or password! Please Try Again')
            return redirect('/login')
    
def logout(request): #log out function
    request.session.clear()
    return redirect('/login')