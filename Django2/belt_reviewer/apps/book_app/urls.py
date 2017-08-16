from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book$', views.add_book),
    url(r'^add_book_process$', views.add_book_process),
    url(r'^logout$', views.log_out),
    url(r'^books/(?P<book_id>\d+)$', views.books, name="books_page"),
    url(r'^users/(?P<review_user_id>\d+)$', views.users),
    url(r'^add_review/(?P<book_id>\d+)$', views.add_review),
    url(r'^delete/(?P<review_id>\d+)$', views.delete),

]
