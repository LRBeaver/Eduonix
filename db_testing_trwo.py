__author__ = 'lyndsay.beaver'
import sqlite3 as sql

def create_market():
    #market= {'ABC':rnd.randint(10,20), 'DEF': rnd.randint(10,20), 'XYZ': rnd.randint(10,20)}
    stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    #prices = []

    #for x in range(len(stocks)):
        #prices.append(rnd.randint(10,20))

    #market = dict(zip(stocks,prices))
    return stocks


def populate_db_w_tickers():
    db1_cursor.execute('CREATE TABLE stocks(ticker TEXT)')
    connection = sql.connect('tickers.db')
    with connection:
        ticker_names = create_market()
        cursor = connection.cursor()
        for ticker in ticker_names[1:-1]:
            if ticker == ['']:
                print('\n    Empty tuple found; skipping.\n')
                continue
            cursor.execute(
                '''INSERT INTO ticker VALUES''' +
                str(tuple(ticker_names)))

populate_db_w_tickers()