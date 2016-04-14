__author__ = 'lyndsay.beaver'

import random as rnd

stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PDQ', 'XYZ']
prices = []

for x in range(len(stocks)):
    prices.append(rnd.randint(10,20))

#print(stocks)
#print(prices)

# for y in range(len(stocks)):
#     print("The price of ", stocks[y] + ' is: ', prices[y])

#for z in range(len(stocks)):
market = dict(zip(stocks,prices))
#market.sort()

print(market)