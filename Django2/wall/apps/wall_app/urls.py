from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.wall_message_create),
    url(r'^process2/(?P<id>\d+)$', views.wall_comment_create),   
    url(r'^logout$', views.log_out),     
]
