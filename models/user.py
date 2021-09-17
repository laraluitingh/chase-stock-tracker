from database import sql_select, sql_write, sql_select_without_params
import yahoo_fin.stock_info as si
import requests
import bcrypt


class User:
    def __init__(self, id, first_name, last_name, email, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


def get_user(email):
    results = sql_select(
        "SELECT id, first_name, last_name, email, password_hash FROM users WHERE email=%s", [email])
    for row in results:
        user = User(row[0], row[1], row[2], row[3], row[4])
    return user


def insert_user(email, first_name, last_name, password):
    password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
    sql_write("INSERT INTO users(email, first_name, last_name, password_hash) VALUES(%s, %s, %s, %s)", [
              email, first_name, last_name, password_hash])


def get_user_by_id(id):
    results = sql_select(
        "SELECT id, first_name, last_name, email, password_hash FROM users WHERE id=%s", [id])
    for row in results:
        user = User(row[0], row[1], row[2], row[3], row[4])
    return user


def update_user(first_name, last_name, email, user_id):
    sql_write("UPDATE users set first_name=%s, last_name=%s, email=%s WHERE id=%s", [
              first_name, last_name, email, user_id])


def see_if_email_exists(email):
    results = sql_select("SELECT * FROM users WHERE email=%s", [email])
    if(results == []):
        return True
    else:
        return False

def check_email_password(email,password):
    try:
        password_hash = get_user(email).password
        valid = bcrypt.checkpw(password.encode(), password_hash.encode())
        if valid:
            return True
        else:
            return False
    except:
        return False


