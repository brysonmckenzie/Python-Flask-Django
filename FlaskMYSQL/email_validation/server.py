from flask import Flask

from mysqlconnection import MySQLConnector

app = Flask(__name__)

mysql = MySQLConnector(app, "emailsdb")


print mysql.query_db("SELECT * FROM emailsdb")

app.run(debug=True)
