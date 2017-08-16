# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    
    current = {   
        
        'date':datetime.now()
    }

    return render(request,'datetime_app/index.html', current)


