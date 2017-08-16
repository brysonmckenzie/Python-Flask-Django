from django.conf.urls import url

from . import views



urlpatterns = [


    url(r'^$', views.index),
    url(r'^login_process$', views.login_process),
    url(r'^registration_process$', views.registration_process),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    

    
]
