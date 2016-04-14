__author__ = 'lyndsay.beaver'

import sqlite3 as sq1

database1 = sq1.connect('test3.db')

db1_cursor = database1.cursor()

cmd = 'CREATE TABLE stocks(ticker TEXT, price INTEGER, shares INTEGER, cost INTEGER)'
cmd2 = 'INSERT INTO stocks(ticker, price, shares) VALUES("ABC", 13, 10, cost)'
cmd3 = 'SELECT ticker, price, shares, cost FROM stocks'

db1_cursor.execute(cmd)
db1_cursor.execute(cmd2)
db1_cursor.execute(cmd3)

database1.commit()

for x in db1_cursor:
    print(x)