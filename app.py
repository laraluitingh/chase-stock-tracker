
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request
import psycopg2
from werkzeug.utils import redirect
import bcrypt
import yahoo_fin.stock_info as si
import requests
import pandas as pd
import json
import os


from models.user import get_user, insert_user, get_user_by_id, update_user, see_if_email_exists, check_email_password
from models.stock import get_stock
from models.watchedStock import addToWhatchList, get_whatchlist, delete_from_whatchlist, most_whatched


SECRET_KEY = os.environ.get("SECRET_KEY", "pretend key for testing only")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

DB_URL = os.environ.get("DATABASE_URL", "dbname=chase-stocks")


@app.route('/')
def getIndexPage():
    data = si.get_day_gainers()
    active_stocks = json.loads(data.to_json(orient='records'))
    print(active_stocks)
    print(type(active_stocks))
    most_popular_stocks = most_whatched()
    most_whatched_stocks = []
    for stock in most_popular_stocks:
        stock_class = get_stock(stock)
        most_whatched_stocks.append(stock_class)
    print(most_whatched)
    return render_template('index.html', most_whatched_stocks=most_whatched_stocks, active_stocks=active_stocks)


@app.route('/login_action', methods=['POST'])
def getLoginPageAction():
    email = request.form.get('email')
    password = request.form.get('password')
    exist=check_email_password(email, password)
    if exist:
         session['user_id'] = get_user(email).id
         return redirect('/account')
    else:
        return render_template('account.html', message=False)



@app.route('/signup')
def getSignUpPage():
    return render_template('signup.html')


@app.route('/signup_action', methods=['POST'])
def insertUser():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    valid = see_if_email_exists(email)
    if first_name == "" or last_name == "" or email == "" or password == "":
        message = "Please fill in all fields"
        incorrect = True
        return render_template('signup.html', message=message, incorrect=incorrect)
    elif first_name != "" and last_name != "" and email != "" and password != "" and valid:
        print(first_name)
        insert_user(email, first_name, last_name, password)
        session['user_id'] = get_user(email).id
        return redirect('/account')
    elif valid == False:
        message = "You have already used this email address to sign up"
        incorrect = True
        return render_template('signup.html', message=message, incorrect=incorrect)


@app.route('/account')
def getProfile():
    user_id = session.get('user_id')
    if user_id == None:
        return render_template('account.html')
    else:
        user = get_user_by_id(user_id)
        whatched_stocks = get_whatchlist(user_id)
        whatchlist = []
        for row in whatched_stocks:
            symbol = row.whatchlist
            stock = get_stock(symbol)
            whatchlist.append(stock)
        return render_template('profile.html', whatchlist=whatchlist, user=user)


@app.route('/search')
def getSearchFunction():
    return render_template('search.html')


@app.route('/search-action')
def searchStock():
    stock = request.args.get('stock')
    stock_data = get_stock(stock)
    if(stock_data == False):
        return render_template('search.html', message="Stock symbol does not exist")
    else:
        user_id = session.get('user_id')
        print(user_id)
        if (user_id == None):
            stock_search = True
            user = False
            return render_template('search.html', stock_data=stock_data, stock_search=stock_search, user=user)
        else:
            stock_search = True
            user = True
            return render_template('search.html', stock_data=stock_data, stock_search=stock_search, user=user)


@app.route('/add_to_whatchlist', methods=['POST'])
def add_to_whatchlist():
    user_id = session.get('user_id')
    print(user_id)
    stock_code = request.form.get('stock_code')
    addToWhatchList(stock_code, user_id)
    return redirect(f'/search-action?stock={stock_code}')


@app.route('/logout')
def log_out():
    session.clear()
    print("clearing cookie")
    return redirect('/account')


@app.route('/edit-profile')
def edit_profile():
    user_id = session.get('user_id')
    user = get_user_by_id(user_id)
    return render_template('editProfile.html', user=user)


@app.route('/update_user', methods=['POST'])
def updateUser():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    user_id = session.get('user_id')
    update_user(first_name, last_name, email, user_id)
    return redirect('/account')


@app.route('/delete_from_whatchlist/<symbol>')
def deleteFromWhatchlist(symbol):
    user_id = session.get('user_id')
    delete_from_whatchlist(user_id, symbol)
    return redirect('/account')


if __name__ == "__main__":
    app.run(debug=True)
