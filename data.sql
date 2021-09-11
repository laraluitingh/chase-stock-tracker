 CREATE table users (id SERIAL PRIMARY KEY, 
 email varchar(100) NOT NULL UNIQUE, 
 first_name varchar(50) NOT NULL, 
 last_name varchar(50) NOT NULL, 
 password_hash TEXT NOT NULL);