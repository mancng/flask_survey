from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    print "POST!!"
    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comments = request.form['comments']
    return render_template('result.html', name = name, language = language, location = location, comments = comments)

app.run(debug=True)