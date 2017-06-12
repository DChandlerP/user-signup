from flask import Flask, request, redirect, render_template
import re
import os

app = Flask(__name__)
app.config['DEBUG'] == True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]
    if is_username_valid(username):
        pass
    else:
        pass
    if does_pw_match(password):
        pass
    else:
        pass
    if is_email_valid(email):
        pass
    else:
        pass
    
    
@app.route("/welcome")
    return render_template("welcome.html")

def does_pw_match(password, verify):
    return password == verify

def is_email_valid(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is not None

def is_username_valid(username):
    return re.match(r'^[\S]{3,20}$', username) is not None


app.run()