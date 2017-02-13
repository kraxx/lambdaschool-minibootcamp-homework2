import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

#creates response to an http request
#when you hit this route, it runs the below:
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return 'October 16 1990'

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    return str(num1 * num2)

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/favoritefoods')
def favoritefoods():
    return jsonify('potatoes', 'carrots', 'peas')
