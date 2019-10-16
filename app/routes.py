from flask import render_template
from flask import Flask, render_template, redirect, url_for,request
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Mr Johns code should be here ??????
@app.route('/test')
def test():
    print ("Hello ")
   