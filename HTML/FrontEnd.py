# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:46:39 2020

@author: CSIT
"""

from flask import Flask, render_template
from UserLogFlask import __main__

app = Flask(__name__)

@app.route('/') #@route decorator
def index():
#    inputstr = input("Enter yeller: ")
#    print(inputstr.upper())
    return "Student log in program"

@app.route('/studentFile')
def output():
    lifetime_dict = {}
    allStr = ""
    sID = 0
    
@app.route('/studentLogIn', methods=["GET", "POST"])
def logIn_page():
    return '''
        <html>
        <head>
        <title>Open Lab Login</title>
        <link rel="stylesheet" type="text/css" href="style.css">
            <body>            
            <div class="loginbox">            
            <img src="avatar2.png" class="avatar">
            <h1>Login Here</h1>            
            <form>            
            <p><center>Enter Palomar Student ID</center></p>
            <input type="text" name="" placeholder="ID">
            <p><input type="submit" value="Submit" /></p>            
            </form>        
            </div>
            </body>
        </head>
    '''


if __name__ == ('__main__'):
    app.run()
    
