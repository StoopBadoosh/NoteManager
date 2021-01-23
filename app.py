from flask import Flask, render_template,request,redirect,flash
from flask_pymongo import PyMongo
import os

#here we are creating our flask app
app=Flask(__name__)
mongostring=os.environ.get('MONGO_URI')
if mongostring=='None':
    print('running on local server')
    file = open(".env", "r")
    connection_string = file.read()
    connection_string = connection_string.strip()
    file.close()
    app.config['MONGO_URI'] = connection_string
else:
    print('running on heroku server')
    app.config['MONGO_URI'] = mongostring

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

@app.route('/shownotes')
def shownotes():
    notes={}
    find = mongo.db.note_manager.find()
    for loop in find:
        name=loop['names']
        note=loop['notes']
        notes[name]=note
    print(notes)
    return render_template('shownotes.html', notes=notes)

if __name__ == "__main__":
    app.run()