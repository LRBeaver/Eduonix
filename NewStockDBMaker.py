__author__ = 'lyndsay.beaver'

import sqlite3 as sq1
import random as rnd

def makemarket():
    tickers = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    prices = []
    for x in range(len(tickers)):
        prices.append(rnd.randint(10,20))
    market = dict(zip(tickers,prices))
    print(market)
    return market

def insert(market):

    print(len(market))


    database1 = sq1.connect('stocks5.db')
    db1_cursor = database1.cursor()

    db1_cursor.execute('CREATE TABLE stocks(ticker TEXT, prices TEXT, current TEXT)')

    list = market.keys()
    for i in list:
        tmp1 = i
        tmp2 = market[i]
        tmp3 = 0

        print(tmp1)
        print(tmp2)
        print(tmp3)
        db1_cursor.execute('INSERT INTO stocks VALUES(?,?, ?)', (tmp1, tmp2, tmp3))


    database1.commit()
    db1_cursor.close()
    database1.close()


    #for x in db1_cursor:
        #print(x)

def main():
    passed_market = makemarket()
    action = input('Would you like to fill the DB?')

    if action == 'y':
        print('\n'+"----------------------")
        print('\n'+"Creating Market DB")
        insert(passed_market)

main()