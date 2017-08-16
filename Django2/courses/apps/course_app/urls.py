from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add),
    url(r'^show_delete/(?P<id>\d+)$', views.show_remove),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^home$', views.home),
]
