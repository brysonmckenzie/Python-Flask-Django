from flask import Flask

from mysqlconnection import MySQLConnector
app = Flask(__name__)

mysql = MySQLConnector(app, 'login_registerdb')

print mysql.query_db("SELECT * FROM login_registerdb")
app.run(debug=True)