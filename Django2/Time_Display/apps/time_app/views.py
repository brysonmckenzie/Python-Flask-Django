# -*- coding: utf-8 -*-
from __future__ import unicode_literals



from django.shortcuts import render, HttpResponse

from datetime import datetime, timedelta
from pytz import timezone
import pytz
from tzlocal import get_localzone 


def index(request):
    
    context = {


        "time": datetime.now(pytz.timezone('US/Pacific'))

    }
    return render(request, 'index.html', context)


