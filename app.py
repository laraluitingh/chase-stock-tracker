
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request
import psycopg2
from werkzeug.utils import redirect
import bcrypt

from models.model import get_user, insert_user


app = Flask(__name__)

app.config['SECRET_KEY'] = '123Lara'



@app.route('/')
def getIndexPage():
    return render_template('index.html')
        

@app.route('/login')
def getLoginPage():
        return render_template('login.html')

@app.route('/login_action', methods=['POST'])
def getLoginPageAction():
        email=request.form.get('email')
        password=request.form.get('password')
        try:
                password_hash=get_user(email).password
                valid = bcrypt.checkpw(password.encode(), password_hash.encode())
                if valid:
                        session['user_id']=get_user(email).id
                        return redirect('/')
                else:
                        render_template('login.html', message=False)
        except:
       
                return render_template('login.html', message=False)

@app.route('/signup')
def getSignUpPage():
        return render_template('signup.html')


@app.route('/signup_action', methods=['POST'])
def insertUser():
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        email=request.form.get('email')
        password=request.form.get('password')
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        insert_user(email, first_name, last_name, password_hash)
        return redirect('/') 

app.run(debug=True, port=3000)