from flask import (Flask, render_template, g) 

import models
import forms

DEBUG = True
PORT = 8000
HOST = "0.0.0.0"

app = Flask(__name__)
app.secret_key = 'kue1y55t5f7bndfs.nkasdkdjsfgfnj'

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE 
    g.db.connect()

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/')
@app.route('/entries')
def list():
    models.Entry.create_entry(title="Entry 1",
                                 date="6/12/2017",
                                 time_spent=60, 
                                 entry_text="Entry 1 text.",
                                 resources_text="Resources for Entry 1.")
    entry_list = models.Entry.select().limit(10)
    return render_template('index.html', entry_list=entry_list)

'''
CAUSING CONFLICTING URL ERROR FOR SOME REASON 

@app.route('/entries/<int:entry_id>') 
def list(entry_id):
    pass
'''

@app.route('/details/<int:entry_id>')
def details(entry_id):
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
    models.initialize()
    app.run(debug=DEBUG, host=HOST, port=PORT)

    