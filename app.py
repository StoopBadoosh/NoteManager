from flask import Flask, render_template
from flask_pymongo import PyMongo

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
@app.route('/')
def landing_page():
    return render_template('index.html')

app.run()