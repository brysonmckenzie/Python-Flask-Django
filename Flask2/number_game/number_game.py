from flask import Flask, render_template, request, redirect, session
from random import randrange
from flask import Flask

app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    
    if 'message' not in session:
        session['message'] = ''
    
    if 'random' not in session:
        session['random'] = ''

    


    random_num = session['random']

    print "**********"
    print random_num, "THIS IS THE RANDOM NUMBER"
    print "**********"


        
    return render_template('index.html')


@app.route('/random')
def random():
    
    return redirect('/')


@app.route('/process' , methods=['POST'])
def process():
    
    random = int(session['random'])
    
    form_num = int(request.form['number'])

    if form_num < 1 or form_num > 100:
        
        session['message'] = 'invalid number!!!'

        return redirect('/')

    elif random != form_num:
        
        print '************'
        print form_num, 'THIS IS YOUR NUMBER'
        print '************'
        if session['random'] < form_num:

            session['message'] = 'Number is to high'
        else:
            session['message'] = 'Number is to low'

    else:
        
        session['message'] = 'You Win'

        
        random = randrange(1,101)
        session['message'] = 'Play Again?'

        print random, "NEW RANDOM NUMBER"

        return redirect('/')

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    
    if 'random' in session:
        session['random'] = ''

        return redirect('/')
    



app.run(debug = True)