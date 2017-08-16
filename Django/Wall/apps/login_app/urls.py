from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login_process$', views.login_process),
    url(r'^register$', views.register),
    url(r'^registration_process$', views.register_process),
    url(r'^wall$', views.wall),
    url(r'^wall_process$', views.wall_process),
    url(r'^logout$', views.logout),
    
]
