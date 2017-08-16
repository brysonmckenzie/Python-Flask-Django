from flask import Flask, request, redirect, render_template, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)

app.secret_key = 'ThisisaSecret'

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
 
        print request.form
        if len(request.form['first_name']) < 1:
            flash("First Name is invalid?")
            print request.form['first_name']
        elif len(request.form['last_name']) < 1:
            print request.form['last_name']
            flash("Last name is invalid?")
        elif len(request.form['email']) < 1:
            flash("Come on dude, Do you know your password?")
        elif not EMAIL_REGEX.match(request.form['email']):
            flash("Email is invalid")
        elif len(request.form['password_confirmation']) < 1:
            flash("Please confirm your password. Try again?")
        elif request.form['password_confirmation'] != request.form['password']:
            flash("please confirm your password!")
            return redirect('/')
        elif int(request.form['first_name']) or int(request.form['last_name']) == type int:
            flash("No numbers in first name or last name!")
        else:
            flash("You have successfully registered!")
            return redirect('/')
        

app.run(debug = True)