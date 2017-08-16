from flask import Flask, redirect, request, session, render_template, flash

app = Flask(__name__)

app.secret_key = 'ThisisaSecret'

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/results')
def results():
    
    session['form_data'] = ''

    return render_template('result.html', formData = session['formData'])

@app.route('/process', methods=['POST'])
def process():
    
    session['formData'] = request.form
    print session['data']
   

    
    print '***********'
    print request.form 
    print '***********'

    if len(request.form['name']) < 1:
        
        flash("Name cannot be empty!")

        return redirect('/')

    elif len(request.form['comment']) < 1:
        
        flash("Name cannot be empty!")

        return redirect('/')

    elif len(request.form['comment']) > 120:

        flash("You have too many characters!!!")

        return redirect('/')
    
    else:
        
        return redirect('/results')



@app.route('/homepage')
def homepage():
    
    return redirect('/')




app.run(debug = True)