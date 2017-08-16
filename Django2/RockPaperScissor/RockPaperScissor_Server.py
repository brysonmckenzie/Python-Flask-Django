from random import randrange

from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if 'win' not in session:
        session['win'] = 0

    if 'loss' not in session:
        session['loss'] = 0

    if 'tie' not in session:
        session['tie'] = 0
    
    if 'outcome' not in session:
        session['outcome'] = ''
           
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    randomNum = randrange(0,4)
    print randomNum
    if 'rock' in request.form:
        userNum = 1
    elif 'paper' in request.form:
        userNum = 2
    else:
        userNum = 3

    if (userNum == randomNum): 
        session['outcome'] = "Tied!!!!"
        session['tie'] += 1
      

    elif (userNum == 1 and randomNum == 2): 
        session['outcome'] = "Your rock was covered in paper, causing you to lose velocity and burn out as you entered the Earth's atmoshpere!!"
        session['loss'] += 1
        

    elif (userNum == 1 and randomNum == 3): 
        session['outcome'] = "Your rock beat scissors..."
        session['win'] += 1
         
        
    elif (userNum == 2 and randomNum == 1): 
        session['outcome'] = "Your paper won against rock..."
        session['win'] += 1
        

    elif (userNum == 2 and randomNum == 3): 
        session['outcome'] = "Your paper was eviscerated by scissors!!!"
        session['loss'] += 1
        

    elif (userNum == 3 and randomNum == 1): 
        session['outcome'] = "Your scissors lost against rock!!!"
        session['loss'] += 1
        

    elif (userNum == 3 and randomNum == 2): 
        session['outcome'] = "Your scissors tore up the paper..."
        session['win'] += 1
        
    
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

app.run(debug = True)
