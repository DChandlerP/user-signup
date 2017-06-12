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
    username_error = ""
    password_error = ""
    email_error = ""

    if not is_username_valid(username):
        username_error = "Invalid Username"
        username = ""
    if not does_pw_match(password, verify):
        password_error = "Passwords didn't match"
        password = ""
        verify = ""
    if not email:
        pass    
    elif not is_email_valid(email):
            email_error = "Invalid Email Address"
            email = ""
    
    if not username_error and not password_error and not email_error:
        return render_template("welcome.html", username = username)
    else:
        return render_template('index.html', username_error=username_error,
            password_error=password_error, email_error= email_error,
            username = username, password = password, email = email,
            verify = verify)
    

def does_pw_match(password, verify):
    return password == verify

def is_email_valid(email):
    return re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) is not None

def is_username_valid(username):
    return re.match(r'^[\S]{3,20}$', username) is not None

app.run()