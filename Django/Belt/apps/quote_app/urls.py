from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration_process$', views.registration_process),
    url(r'^login_process$', views.login_process),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^create_q$', views.create_q),
]