from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^register_process$', views.register_process),
    url(r'^$', views.login),
    url(r'^login_process$', views.login_process),
    ]
