 CREATE table users (id SERIAL PRIMARY KEY, 
 email varchar(100) NOT NULL UNIQUE, 
 first_name varchar(50) NOT NULL, 
 last_name varchar(50) NOT NULL, 
 password_hash TEXT NOT NULL);

 CREATE TABLE whatched_stocks (
     stock_code TEXT,
     id INTEGER NOT NULL REFERENCES users(id) 
 );