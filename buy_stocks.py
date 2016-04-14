__author__ = 'lyndsay.beaver'

import random as rnd
balance = 10000

def create_market():
    #market= {'ABC':rnd.randint(10,20), 'DEF': rnd.randint(10,20), 'XYZ': rnd.randint(10,20)}
    stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10,20))

    market = dict(zip(stocks,prices))
    return market

#market= {'ABC':rnd.randint(10,20), 'DEF': rnd.randint(10,20), 'XYZ': rnd.randint(10,20)}
#print(market)

def buy_stocks(passed_market, balance):
    print(balance)
    #cash_available = 10000
    print('You have : $', balance)
    print(passed_market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: ', passed_market[choice])
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(passed_market[choice])
    print(cost)
    balance= balance-cost
    print(balance)

passed_market=create_market()
buy_stocks(passed_market, balance)
#print(passed_market)
