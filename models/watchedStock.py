from database import sql_select, sql_write, sql_select_without_params
import yahoo_fin.stock_info as si
import requests


class UserWatchlist:
    def __init__(self, user_id, whatchlist):
        self.user_id = user_id
        self.whatchlist = whatchlist


def addToWhatchList(stock_code, user_id):
    results = sql_select("SELECT stock_code, id FROM whatched_stocks WHERE stock_code=%s AND id=%s", [
                         stock_code, user_id])
    print(results)
    if(results == []):
        sql_write("INSERT INTO whatched_stocks(stock_code, id) VALUES(%s,%s)", [
                  stock_code, user_id])


def get_whatchlist(id):
    results = sql_select(
        "SELECT id, stock_code FROM whatched_stocks WHERE id=%s", [id])
    whatchlist = []
    for row in results:
        stock_whatched = UserWatchlist(row[0], row[1])
        whatchlist.append(stock_whatched)
    return whatchlist


def delete_from_whatchlist(id, stock_code):
    sql_write("DELETE FROM whatched_stocks WHERE id=%s AND stock_code=%s", [
              id, stock_code])


def most_whatched():
    results = sql_select_without_params(
        "SELECT stock_code, COUNT(stock_code) AS Value_Occurence FROM whatched_stocks GROUP BY stock_code ORDER BY Value_Occurence DESC LIMIT 10;")
    most_whatched = []
    for row in results:
        most_whatched.append(row[0])
    print(most_whatched)
    return most_whatched
