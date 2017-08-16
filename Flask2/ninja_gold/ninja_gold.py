from flask import Flask, redirect, render_template, session, request
 
from random import randrange

import datetime

app = Flask(__name__)

app.secret_key = "ThisistheSecretKey"

@app.route('/')
def index():
    
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []
    
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

  
    if request.method == 'POST':
        if request.form['location'] == 'farm':
            count = randrange(10,20)
            session['gold'] += count
            activity = session['activities']
            # activity.append("Earned ", count, "golds from the farm!",datetime.datetime.now())
        
        if request.form['location'] == 'cave':
            count = randrange(5,11)
            session['gold'] += count
            # activity.append("Earned ", count, "golds from the casino!",datetime.datetime.now())        
        if request.form['location'] == 'house':
            count = randrange(2,6)
            session['gold'] += count
            activity = session['activities']
            # activity.append("Earned ", count, "golds from the house!",datetime.datetime.now())
        
        if request.form['location'] == 'casino':
            count = randrange(-50,50)
            if count > 0:
                session['gold'] += count
                a = "Earned ", count, "golds from the house!",datetime.datetime.now()
                # session['activities'].append(a)
            if count < 0:
                session['gold'] -= count
                a = "Entered a casino and lost ", count, "golds....Ouch!!!",datetime.datetime.now()
                # session['activities'].append(a)

        return redirect('/')

    return redirect('/')

@app.route('/reset')
def reset():
    
    session.clear()

    return redirect('/')
        




app.run(debug = True)
