from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/about')
def aboutme():
    
    return render_template('aboutme.html')

@app.route('/projects')
def page():
    
    return render_template('page.html')

app.run(debug=True)
