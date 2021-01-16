from flask import Flask, render_template,request,redirect,flash
from flask_pymongo import PyMongo
import os

#here we are getting the connection string
file=open(".env","r")
connection_string=file.read()
connection_string=connection_string.strip()
file.close()

#here we are creating our flask app
app=Flask('Anish')
app.config['MONGO_URI']=connection_string

#here we are combining our flask object with mongodb
mongo=PyMongo(app)
@app.route('/', methods=['GET','POST'])
def landing_page():
    if request.method=='GET':
        return render_template('index.html')
    else:
        return redirect('/enternotes')


@app.route('/enternotes', methods=['GET','POST'])
def enternotes():
    if request.method=='GET':
        return render_template('enternotes.html')
    else:
        input_for_note=request.form['note'].strip()
        input_for_name=request.form['name'].strip()
        full_notes={'notes':input_for_note,'names':input_for_name}
        mongo.db.note_manager.insert_one(full_notes)
        return redirect('/')

@app.route('/shownotes', methods=['GET','POST'])
def shownotes():
    if request.method=='GET':
        return render_template('shownotes.html')
app.run()