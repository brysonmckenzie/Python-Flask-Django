from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^login_process$', views.login_process),
    url(r'^register_process$', views.register_process),
    url(r'^add_task$', views.add_task),
    url(r'^update/(?P<id>\d+)$', views.show_update),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^update_process/(?P<id>\d+)$', views.update_process),
    url(r'^logout$', views.logout),
]

