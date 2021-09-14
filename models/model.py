from database import sql_select, sql_write
import yahoo_fin.stock_info as si
import requests
import asyncio



class User:
    def __init__(self,id, first_name, last_name, email, password):
        self.id=id
        self.first_name = first_name   
        self.last_name = last_name
        self.email = email
        self.password =password

class Stock:
    def __init__(self,name, short_name, symbol, currency, market_price, market_change, market_change_percent, previous_close, market_open, avg_volume, w_range, day_range):
        self.name=name
        self.short_name = short_name   
        self.symbol = symbol
        self.currency = currency
        self.market_price = market_price
        self.market_change = market_change
        self.market_change_percent =market_change_percent
        self.previous_close = previous_close
        self.market_open = market_open
        self.avg_volume = avg_volume
        self.w_range=w_range
        self.day_range=day_range

class News:
    def __init__(self,id, title, summary, pubdate, url, image):
        self.id = id
        self.title = title   
        self.summary = summary
        self.pubdate = pubdate
        self.url = url
        self.image=image


def get_user(email):
  results=sql_select("SELECT id, first_name, last_name, email, password_hash FROM users WHERE email=%s", [email])
  for row in results:
      user=User(row[0], row[1], row[2], row[3], row[4])
  return user

def insert_user(email, first_name, last_name, password):
    sql_write("INSERT INTO users(email, first_name, last_name, password_hash) VALUES(%s, %s, %s, %s)", [email, first_name, last_name, password])

def get_stock(stock):
    data=si.get_quote_data(stock)
    print(data["regularMarketChangePercent"])
    stock=Stock(data["fullExchangeName"],
    data["shortName"],
    data["symbol"],
    data["currency"],
    data["regularMarketPrice"],
    data["regularMarketChange"],
    data["regularMarketChangePercent"],
    data["regularMarketPreviousClose"],
    data["regularMarketOpen"],
    data["averageDailyVolume3Month"],
    data["fiftyTwoWeekRange"],
    data["regularMarketDayRange"]
    )
    return stock

#need to delete too slow
# def get_NewsList():
#     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
#     querystring = {"snippetCount":"5"}
#     payload = ""
#     headers = {
#         'content-type': "text/plain",
#         'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
#         'x-rapidapi-key': "945e1daf09msh480bc50d04ff36ep1c4656jsne375a18f58c8"
#         }

#     response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#     data=response.json()
#     array_of_news=data["data"]["main"]["stream"]
#     news_items=[]
#     for i in array_of_news:
#         news={
#             "id":i["content"]["id"],
#             "title": i["content"]["title"],
#             "pub-date": i["content"]["pubDate"],
#             "picture": i["content"]["thumbnail"]["resolutions"][0]["url"]
#             }
#         news_items.append(news)
#     return news_items

#need to delete too slow

# def get_NewsList(stock_code="none"):
#     url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/list"
#     if stock_code=="none":
#         querystring = {"snippetCount":"1"}
#     else:
#         querystring = {"snippetCount":"5","s":stock_code}
#     payload = ""
#     headers = {
#         'content-type': "text/plain",
#         'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
#         'x-rapidapi-key': "945e1daf09msh480bc50d04ff36ep1c4656jsne375a18f58c8"
#     }

#     response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
#     data=response.json()
#     array_of_news=data["data"]["main"]["stream"]
#     news_items=[]
#     for i in array_of_news:
#         id=i["content"]["id"]
#         url2 = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/news/v2/get-details"
#         querystring2 = {"uuid":id ,"region":"US"}
#         headers2 = {
#             'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
#             'x-rapidapi-key': "945e1daf09msh480bc50d04ff36ep1c4656jsne375a18f58c8"
#             }
#         response2 = requests.request("GET", url2, headers=headers2, params=querystring2)
#         final_data=response2.json()['data']['contents'][0]['content']
#         news=News(final_data["id"],
#         final_data["title"],
#         final_data["summary"],
#         final_data["pubDate"],
#         final_data["canonicalUrl"]["url"],
#         i["content"]["thumbnail"]["resolutions"][0]["url"]
#         )
#         news_items.append(news) 
#     return news_items


def addToWhatchList(stock_code, user_id):
    sql_write("INSERT INTO whatched_stocks(stock_code, id) VALUES(%s, %s)", [stock_code, user_id])



        

       







