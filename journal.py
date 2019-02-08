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

@app.route('/entries')
@app.route('/entries/<int:entry_id>')
def view_entries(entry_id):
    pass

@app.route('/entries/edit/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    pass

@app.route('/entries/delete/<int:entry_id>', methods=['GET', 'POST'])
def delete_entry(entry_id):
    pass

@app.route('/entry', methods=['GET', 'POST'])
def create_entry():
    pass 



if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)