# chase-stock-tracker

Website that allows users to track stocks, and keep up to date with the latest financial data

Mobile-friendly

Heroku website: https://quiet-citadel-28182.herokuapp.com/

## Features

- Look up the most traded stocks
- User can login and sign up
- User can watch specific stocks, indexes and cryptocurrencies
- User can view profile with the stocks they are watching
- Users can remove stocks from their watchlist
- Show the top 10 most watched stocks on the platform

## Technologies
1. Python Flask
2. CSS
3. HTML
4. Javascript
5. Yahoo_fin api

## Steps to deploy wesbite locally 

1. Inside project file create create a virtual environment

` python -m venv venv `

2. Activate the virtual environment

`source venv/bin/activate`

3. Install postgress https://www.postgresql.org/

4. Install the following: flask, psycopg2, bcrypt. Run the following commands in your terminal

     - `pip intall flask`
     - `pip intall psycopg2`
     - `pip intall bcrypt`

5. Install th yahoo_fin api http://theautomatic.net/yahoo_fin-documentation/#installation

`pip install yahoo_fin`
`pip install requests_html`

6. Create local database in your terminal:

` createdb chase-stocks`

7. Create tables

   - `psql chase-stocks`
   - CREATE table users (id SERIAL PRIMARY KEY, 
     email varchar(100) NOT NULL UNIQUE, 
     first_name varchar(50) NOT NULL, 
     last_name varchar(50) NOT NULL, 
     password_hash TEXT NOT NULL);
   - CREATE TABLE whatched_stocks (
     stock_code TEXT,
     id INTEGER NOT NULL REFERENCES users(id));
    

 ## Possible Future Imrovements
  - Write Cleaner more readible code
  - Increase website speed
  - Have users confirm their emails before they can succesfully signup
  - Allow users to track stock prices and be notified in realtime if stock price reaches an set price
  - Have stock prices adjust on the website in realtime without having the page to reload 
  - Provide Additional Financial data

## Current bugs
- Users can delete their name, and email
- Searchbox's dropdown menu peroidically stops working 


