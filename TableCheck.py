__author__ = 'lyndsay.beaver'
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
    #stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    print(len(market))
    print(market)
    list = market.keys()
    for i in list:
        tmp1 = i
        tmp2 = market[i]
        #print(i, market[i])
        print(tmp1)
        print(tmp2)


def main():
    passed_market = makemarket()
    action = input('Would you like to fill the DB?')

    if action == 'y':
        print('\n'+"----------------------")
        print('\n'+"Creating Market DB")
        insert(passed_market)

main()