from flask import Flask, render_template
app=Flask('Anish')

@app.route('/')
def landing_page():
    return render_template('index.html')

app.run()