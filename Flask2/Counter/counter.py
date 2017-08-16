from flask import Flask, redirect, request, render_template, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    
    if 'count' not in session:
        session['count'] = 1

    return render_template('index.html', count = session['count'])

@app.route('/process', methods=['POST'])
def count():
            session['count'] += 2

            return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
            session['count'] = 1

            return redirect('/')


app.run(debug = True)