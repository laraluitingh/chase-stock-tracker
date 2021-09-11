from database import sql_select, sql_write


class User:
    def __init__(self,id, first_name, last_name, email, password):
        self.id=id
        self.first_name = first_name   
        self.last_name = last_name
        self.email = email
        self.password =password

def get_user(email):
  results=sql_select("SELECT id, first_name, last_name, email, password_hash FROM users WHERE email=%s", [email])
  for row in results:
      user=User(row[0], row[1], row[2], row[3], row[4])
  return user

#  CREATE table users (id SERIAL PRIMARY KEY, 
#  email varchar(100) NOT NULL UNIQUE, 
#  first_name varchar(50) NOT NULL, 
#  last_name varchar(50) NOT NULL, 
#  password_hash TEXT NOT NULL);

def insert_user(email, first_name, last_name, password):
    sql_write("INSERT INTO users(email, first_name, last_name, password_hash) VALUES(%s, %s, %s, %s)", [email, first_name, last_name, password])

