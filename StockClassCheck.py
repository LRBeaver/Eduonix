__author__ = 'lyndsay.beaver'

class Stock:
    def __init__(self, name, ticker, price):
        self.name = name
        self.ticker = ticker
        self.price = price

stock1 = Stock("Apple", "AAPL", 300)

def ShowStock(self):
    print("------")
    print("The first stock is " + self.name + ' it\'s price is: ' + str(self.price))

ShowStock(stock1)