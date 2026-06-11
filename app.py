from flask import Flask, render_template, redirect, request

# configuring app
app = Flask(__name__)
# secret key for flask flash notifications 
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def index():
    return render_template('generate.html')

@app.route('/history')
def index():
    return render_template('history.html')