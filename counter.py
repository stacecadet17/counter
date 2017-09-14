from flask import Flask, request, redirect, render_template, session
app = Flask(__name__)
app.secret_key = "unicorns"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template('index.html')

@app.route('/addtwo')
def addtwo():
    session["count"] += 1
    return redirect('/')

@app.route('/reset')
def reset():
    session["count"] = 0
    return redirect('/')


app.run(debug = True)
