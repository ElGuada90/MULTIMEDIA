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


##### SERIES FRIENDS
#################################################################################

@app.route('/friendst7c1')
def friendst7c1():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst7c1.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst7c2')
def friendst7c2():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst7c2.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst7c3')
def friendst7c3():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst7c3.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
##### SERIES FRIENDS TEMPORADA 8
#################################################################################

@app.route('/friendst8c1')
def friendst8c1():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst8c1.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst8c2')
def friendst8c2():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst8c2.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst8c3')
def friendst8c3():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst8c3.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
##### SERIES FRIENDS TEMPORADA 9
#################################################################################

@app.route('/friendst9c1')
def friendst9c1():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst9c1.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst9c2')
def friendst9c2():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst9c2.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst9c3')
def friendst9c3():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst9c3.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
##### SERIES FRIENDS TEMPORADA 10
#################################################################################

@app.route('/friendst10c1')
def friendst10c1():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst10c1.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst10c2')
def friendst10c2():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst10c2.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)
    
@app.route('/friendst10c3')
def friendst10c3():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %I:%M:%S %p")
    return render_template(
        "series/friends/friendst10c3.html",
        title = "EG90 Series",
        message = "Top Series ", 
        content = formatted_now)