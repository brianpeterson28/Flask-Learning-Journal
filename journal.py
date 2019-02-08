from flask import (Flask, render_template) 

import models
import forms

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entries', methods=['GET', 'POST'])
def entries():
    pass

@app.route('/entry')
def entry():
    pass 


if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)