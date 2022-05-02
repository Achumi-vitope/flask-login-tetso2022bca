import imp
from django.shortcuts import render
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from pip import main
import sys
app = Flask(__name__, template_folder='template')

app.secret_key = '2292015165'


app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2292015165'
app.config['MYSQL_DB'] = 'swl'


mysql = MySQL(app)
@app.route("/")

@app.route('/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('Home.html', msg = msg)
        else:
            msg = 'Incorrect username or password!'
    return render_template('login.html', msg = msg)
  


REGISTRANTS = [
    "vitopeachumi@tetsocollege.org",
    "default",
    "akani@tetsocollege.org",
    "vitolu@tetsocollege.org",
    "phuyeka@tetsocollege.org",
    "zukathungh@tetsocollege.org",
    "sungjemrenla@tetsocollege.org",
    "hechikhum@tetsocollege.org",
    "allenkath@tetsocollege.org",
    "skinimi@tetsocollege.org",
    "jenithung@tetsocollege.org",
    "achah@tetsocollege.org",
    "chetei@tetsocollege.org",
    "nokman@tetsocollege.org",
    "akumtoshilemtur1@tetsocollege.org",
    "zavung@tetsocollege.org",
    "kevisetounon@tetsocollege.org",
    "khathru@tetsocollege.org",
    "thephen@tetsocollege.org",
    "senti@tetsocollege.org",
    "vsekhose@tetsocollege.org",
    "avirup@tetsocollege.org",
    "huka@tetsocollege.org",
    "aruso@tetsocollege.org",
    "chingnyei@tetsocollege.org",
    "medovinuo@tetsocollege.org",
    "asu@tetsocollege.org",
    "mutuzo@tetsocollege.org",
    "vivikaliyeptho@tetsocollege.org",
    "abokaz@tetsocollege.org",
    "nayan@tetsocollege.org",
    "nangshiba@tetsocollege.org",
    "imchenmeren@tetsocollege.org"
]
@app.route('/sem6', methods=['GET','POST'])
def sem6():
    return render_template('sem6.html')

@app.route('/sem5', methods=['GET','POST'])
def sem5():
    return render_template('sem5.html')
@app.route('/sem4', methods=['GET','POST'])
def sem4():
    return render_template('sem4.html')
@app.route('/sem3', methods=['GET','POST'])
def sem3():
    return render_template('sem3.html')
@app.route('/sem2', methods=['GET','POST'])
def sem2():
    return render_template('sem2.html')

@app.route('/sem1', methods=['GET','POST'])
def sem1():
    return render_template('sem1.html')

@app.route('/register', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        elif email not in REGISTRANTS:
            msg = 'Not a Recognised Email!. Please contact the admin'
        else:
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered! Proceed to sign-in'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg=msg)

if __name__ == "__main__":
    app.run("localhost", 5000)
    
    
    
    

    