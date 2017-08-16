from flask import Flask, render_template, request, redirect 

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')


@app.route('/ninja')
def all_ninjas():
    
    return render_template('all_ninjas.html')


@app.route('/ninja/<color>')
def ninjas(color):
   

    return render_template('ninjas.html', color = color)

app.run(debug=True)

