# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import models, Course 

def index(request):
    
    context = {

        'course': Course.objects.all().order_by('-created_at'),
    }

    return render(request, 'course_app/index.html', context)

def add(request):
    
    server_name = request.POST['html_name']
    server_description = request.POST['html_description']
    
    course = Course.objects.create(name = server_name , description = server_description)
    print '*************',"New Course Created" '********************'
    print course
    return redirect('/')

def show_remove(request,id):

    context = {
        'courses':Course.objects.get(id = id)
    }
    
    

    return render(request, 'course_app/show_remove.html',context)

def remove(request, id):
    if request.method == 'POST':
        course = Course.objects.get(id = id).delete()
        print course
        
    return redirect('/')

def home(request):
    
    if request.method == 'POST':

        return redirect('/')