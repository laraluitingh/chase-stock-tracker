# chase-stock-tracker

Website that allows users to track stocks, and keep up to date with the latest financial data

Heroku website: https://quiet-citadel-28182.herokuapp.com/

## Features

- Can use look the most traded stocks
- User can login and sign up
- User can watch specific stocks, indexes and cryptocurrencies
- User can view profile with the stocks it they are watching
- Users can remove stocks from their watslist
- Show the top 10 most watched stocks on the platform

## Requirements

- Need to install flask, psycopg2, bcrypt
- Stock data is retrieved from the Yahoo_fin api
- Uses python, html and css
- Deployed on Heroku 
- Need to configure secret key on Heroku to deploy
- Need to create local database to deploy locally

## SQL commands to Deploy locally

1. createdb chase-stocks
2.  CREATE table users (id SERIAL PRIMARY KEY, 
 email varchar(100) NOT NULL UNIQUE, 
 first_name varchar(50) NOT NULL, 
 last_name varchar(50) NOT NULL, 
 password_hash TEXT NOT NULL);
3. CREATE TABLE whatched_stocks (
     stock_code TEXT,
     id INTEGER NOT NULL REFERENCES users(id) 
 );

 ## Possible Future Imrovements
  - Write Cleaner more readible code
  - Increase website speed
  - Have users confirm their emails before they can succesfully signup
  - Allow users to track stock prices and be notified in realtime if stock price reaches an set amount
  - Cleaner UI
  - Responsive Ui- Mobile freindly
  - Have stock prices adjust on website in realtime without page having to be reloaded
  - Allow users to get more information from stocks



