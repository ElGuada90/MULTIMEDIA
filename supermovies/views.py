from flask import Flask, render_template
from datetime import datetime
from supermovies import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "index.html",
        title = "EG90  Home",
        message = "Top Stream ",
        content =  formatted_now)
    
    
@app.route('/login')
def login():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "login.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)    
    
@app.route('/series')
def series():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/series.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)    
    
@app.route('/logout')
def logout():
    
    return render_template("index.html",)