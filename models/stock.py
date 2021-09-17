from database import sql_select, sql_write, sql_select_without_params
import yahoo_fin.stock_info as si
import requests


class Stock:
    def __init__(self, name, short_name, symbol, currency, market_price, market_change, market_change_percent, previous_close, market_open, avg_volume, w_range, day_range):
        self.name = name
        self.short_name = short_name
        self.symbol = symbol
        self.currency = currency
        self.market_price = market_price
        self.market_change = market_change
        self.market_change_percent = market_change_percent
        self.previous_close = previous_close
        self.market_open = market_open
        self.avg_volume = avg_volume
        self.w_range = w_range
        self.day_range = day_range


def get_stock(stock):
    try:
        data = si.get_quote_data(stock)
        print(data["regularMarketChangePercent"])
        stock = Stock(data["fullExchangeName"],
                      data["shortName"],
                      data["symbol"],
                      data["currency"],
                      data["regularMarketPrice"],
                      round(data["regularMarketChange"], 2),
                      round(data["regularMarketChangePercent"], 2),
                      data["regularMarketPreviousClose"],
                      data["regularMarketOpen"],
                      data["averageDailyVolume3Month"],
                      data["fiftyTwoWeekRange"],
                      data["regularMarketDayRange"]
                      )
        return stock
    except:
        return False
