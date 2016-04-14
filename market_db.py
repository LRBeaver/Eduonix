__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
import random as rnd

stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
prices = []

for x in range(len(stocks)):
    prices.append(rnd.randint(10,20))

# market = dict(zip(stocks,prices))
# print(market)

database1 = sq1.connect('market3.db')

db1_cursor = database1.cursor()

db1_cursor.execute('CREATE TABLE stocks(ticker TEXT, price INTEGER);')
count = 0
while count != len(stocks):
    db1_cursor.executemany('INSERT INTO stocks (ticker, price) VALUES (:stocks, :prices)', (stocks,), (prices,))
    count += 1

# cmd = 'CREATE TABLE stocks(ticker TEXT, price INTEGER)'
# #cost=shares*price
# cmd2 = 'INSERT INTO stocks(ticker, price) VALUES(stock, 13)'
# cmd3 = 'SELECT ticker, price FROM stocks'

# db1_cursor.execute(cmd)
# for count in len(stocks()):
#     db1_cursor.execute(cmd2)
# db1_cursor.execute(cmd3)

database1.commit()
db1_cursor.close()
database1.close()


for x in db1_cursor:
    print(x)