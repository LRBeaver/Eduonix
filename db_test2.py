__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
import random as rnd
tickers = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']


def insert(array):
    stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    print(len(stocks))
    print(len(stocks,))

    database1 = sq1.connect('stocks3.db')
    db1_cursor = database1.cursor()

    db1_cursor.execute('CREATE TABLE stocks(ticker TEXT)')
    count = 0
    while count != len(stocks):
        db1_cursor.executemany('INSERT INTO stocks VALUES (?)', (stocks,))
        count += 1

    database1.commit()
    db1_cursor.close()
    database1.close()


    for x in db1_cursor:
        print(x)

insert(tickers)