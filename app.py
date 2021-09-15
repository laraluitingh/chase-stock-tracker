
from flask import Flask, render_template, request, redirect, session
from flask.wrappers import Request
import psycopg2
from werkzeug.utils import redirect
import bcrypt
import yahoo_fin.stock_info as si
from yahoo_fin import news
import requests
import pandas as pd
import json


from models.model import get_user, insert_user, get_stock, addToWhatchList, get_user_by_id, get_whatchlist


app = Flask(__name__)

app.config['SECRET_KEY'] = '123Lara'


@app.route('/')
def getIndexPage():
    stocks = []
    nasdaq = get_stock('^NDX')
    dow_jones = get_stock('^DJI')
    oil = get_stock('CL=F')
    gold = get_stock('GC=F')
    stocks.append(nasdaq)
    stocks.append(dow_jones)
    stocks.append(gold)
    stocks.append(oil)
    data = si.get_day_most_active()
    active_stocks = json.loads(data.to_json(orient='records'))
    print(type(active_stocks))
    return render_template('index.html', stocks=stocks, active_stocks=active_stocks)


# @app.route('/login')
# def getLoginPage():
#         return render_template('login.html')

@app.route('/login_action', methods=['POST'])
def getLoginPageAction():
    email = request.form.get('email')
    password = request.form.get('password')
    print(get_user(email))
    try:
        password_hash = get_user(email).password
        valid = bcrypt.checkpw(password.encode(), password_hash.encode())
        if valid:
            session['user_id'] = get_user(email).id
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
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    insert_user(email, first_name, last_name, password_hash)
    return redirect('/')


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
    stock_search = True
    news1 = news.get_yf_rss(stock)
    print(news1)
    return render_template('search.html', stock_data=stock_data, stock_search=stock_search)


@app.route('/add_to_whatchlist', methods=['POST'])
def add_to_whatchlist():
    user_id = session.get('user_id')
    stock_code = request.form.get('stock_code')
    addToWhatchList(stock_code, user_id)
    return redirect('/search')


app.run(debug=True, port=3000)
