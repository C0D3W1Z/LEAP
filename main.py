from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/studentresources')
def studentresources():
    return render_template('studentresources.html')

@app.route('/parentresources')
def parentresources():
    return render_template('parentresources.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/schoolapplication')
def schoolapp():
    return render_template('schoolapp.html')

@app.route('/volunteerapplication')
def volunteerapp():
    return render_template('volunteerapp.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if(__name__ == "__main__"):
    app.run(debug=True, port=5000)