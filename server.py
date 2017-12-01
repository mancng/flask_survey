from flask import Flask, render_template, redirect, request, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=["POST"])
def result():
    print "POST!!"
    errors = False
    if len(request.form['name']) < 1:
        flash("Name cannot be empty")
        errors = True
    if len(request.form['comments']) < 1:
        flash("Please leave a comment")
        errors = True
    elif len(request.form['comments']) > 120:
        flash("Comments cannot exceed 120 characters!")
        errors = True

    name = request.form['name']
    language = request.form['language']
    location = request.form['location']
    comments = request.form['comments']

    if errors:
        return redirect('/')
    else:
        return render_template('result.html', name = name, language = language, location = location, comments = comments)

app.run(debug=True)