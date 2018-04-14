# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:11:37 2018

@author: Herbert
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/test_flask/')
def inedx():
    return render_template('login.html')

@app.route('/FlaskTutorial', methods =['POST'])
def success():
    if request.method == "POST":
        email = request.form['email']
        
        print("test")
        return render_template('success.html', email=email)
    else:
        pass
    

if __name__=="__main__":
    app.run()