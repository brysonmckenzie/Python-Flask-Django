# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import User, Book, Author, Review

def  index(request):
    
    context = {
        "current_user":User.objects.get(id = request.session['user_id']),
        "reviews":Review.objects.all(),
        "users":User.objects.all(),
        "books":Book.objects.all(),
        }
    
    return render(request, 'book_app/index.html', context)

def add_book(request):
    context = {
        "books": Book.objects.all()
    }

    
    return render(request, "book_app/add_book.html",context)


def add_book_process(request):
    current_user = request.session['user_id']
    book_title = request.POST['book_title']
    add_author = request.POST['add_author']
    book_review = request.POST['book_review']
    author = request.POST['author']

    rating = request.POST['rating']

    if request.method == 'POST':
        if request.POST['add_author'] == "":
            user = User.objects.get(id=current_user)
            author = Author.objects.create(name=author)
            book = Book.objects.create(title=book_title, author=author)
            Review.objects.create(user=user, review=request.POST['book_review'], rating=request.POST['rating'], book=book)
        else:
            user = User.objects.get(id=current_user)
            author = Author.objects.create(name=add_author)
            book = Book.objects.create(title=book_title, author=add_author)
            Review.objects.create(user=user, review=request.POST['book_review'], rating=request.POST['rating'], book=book)
        

    return redirect("/")

def add_review(request, book_id):
    
    current_user = request.session['user_id']
    
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['current_user'])

        Review.objects.create(rating=request.POST['rating'], review=request.POST['review'], book=book, user=user)


    return redirect('books_page', book_id=book_id)

def books(request, book_id):
   
    current_user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book_id=book_id)

    context = {
        "book": book,
        "reviews": reviews,
        "logged_user": request.session['user_id'],
    }
    return render(request, "belt_review/books.html", context)

def add_review(request, book_id):
    
    if request.method == "POST":
        book = Book.objects.get(id=book_id)
        user = User.objects.get(id=request.session['logged_user'])

        Review.objects.create(rating=request.POST['rating'], review=request.POST['review'], book=book, user=user)


    return redirect('book')

def users(request, review_user_id):
        
    user = User.objects.get(id=review_user_id)
    review_book_titles = Review.objects.filter(book_id=review_user_id)

    rating = Review.objects.filter(user_id=review_user_id)

    if rating > 0:
        rating = len(rating)

    context = {
        "user": user,
        "review": review_book_titles,
        "rating": rating
    }


    return render(request, "belt_review/users.html", context)

def delete(request, review_id):
  

    review = Review.objects.get(id=review_id)
    book_id = review.book.id

    #delete query
    review.delete()

    return redirect('books_page', book_id=book_id)


def log_out(request):
    
    if request.method == 'POST':
        
        request.session.clear()

    return redirect('/login')


    

