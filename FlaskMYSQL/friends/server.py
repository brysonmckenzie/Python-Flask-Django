from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')



print mysql.query_db("SELECT * FROM friends")

@app.route('/')
def index():
    
    all_data = mysql.query_db("SELECT * FROM friends")
    
    
    return render_template('index.html',all_data=all_data)


@app.route('/create', methods=['POST'])
def create():
    
    query = "INSERT INTO friends (name, age, created_at, updated_at) VALUES(:name, :age, NOW(),NOW())"
   

    data = {
        "name": request.form["name"],
        "age": request.form["age"]
            }
    mysql.query_db(query, data)

    
    return redirect('/')




    
app.run(debug=True)