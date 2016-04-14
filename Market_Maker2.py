__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
import random as rnd

#"{:,}".format(value)

starting = 10000
balance = starting
#returned_portfolio = ()
goto_menu = True

def create_market():
    stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10,20))

    market = dict(zip(stocks, prices))
    #print(len(market))
    return market

def insert(market):
    #print("Number of stocks: ", len(market))
    database1 = sq1.connect('stocks' + str(rnd.randint(1,200)) + '.db')
    db1_cursor = database1.cursor()

    db1_cursor.execute('CREATE TABLE stocks(ticker TEXT, prices TEXT, current TEXT)')

    list = market.keys()
    for i in list:
        tmp1 = i
        tmp2 = market[i]
        tmp3 = 0

        db1_cursor.execute('INSERT INTO stocks VALUES(?,?, ?)', (tmp1, tmp2, tmp3))

    database1.commit()
    db1_cursor.close()
    database1.close()

def check_market(market):
    print('\n'+"----------------------")
    print('\n'+"You chose to check the market")
    if 'market' in locals():
        print(market)
    else:
        create_market()


def check_portfolio(owned_portfolio):
    print('\n'+"----------------------")
    print("You chose to check your portfolio")
    print('\n' + "******************")
    if 'returned_balance' in locals():
        current_balance=returned_balance
    else:
        if owned_portfolio == {}:
            print("You own no stocks")
            print("You have ${:,}".format(balance))
        else:
            print('Portfolio: ', owned_portfolio)
            print('Cash: ${:,}'.format(current_balance))

def buy_stocks(passed_market, balance):
    #print(balance)
    #cash_available = 10000
    print('\n'+"----------------------")
    print("You chose to buy stocks")
    print("You have ${:,}".format(balance))
    print(passed_market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: $', passed_market[choice])
    print('\n'+"----------------------")
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(passed_market[choice])
    owned_portfolio={choice:cost}
    print("This transaction will cost: ${:,}".format(cost))
    returned_balance=balance-cost
    print("You now have this much cash left: ${:,}".format(returned_balance))
    print(owned_portfolio)
    return (owned_portfolio, returned_balance)

def sell_stocks(passed_portfolio,balance):
    print('\n'+"----------------------")
    print("You chose to sell stocks")
    sold_ticker=input("What stock would you like to sell?: ")
    if sold_ticker in passed_portfolio:
        print('\n'+"----------------------")
        shares_to_sell=input("How many shares would you like to sell?: ")
        if shares_to_sell <= owned_shares:
            print("Selling x shares:")

def menu(market, owned_portfolio):
    print(owned_portfolio)
    print('\n'+"----------------------")
    print(""" Market game - stocks
        [1] Check the market
        [2] Check your portfolio
        [3] Buy stocks
        [4] Sell stocks
        [5] End the day
        """)

    action = input('What would you like to do?: ')

    if action == '1':
        if 'market' in locals():
            print("Used existing")
            check_market(market)
        else:
            print("Had to make a new one")
            passed_market=create_market()
            check_market(passed_market)

    elif action == '2':
        if 'owned_portfolio' in locals():
            check_portfolio(owned_portfolio)
             #print("You have ${:,}".format(balance))
        else:
            print('\n'+"----------------------")
            print("You own no stocks")
            print("You have ${:,}".format(balance))

    elif action == '3':
        if 'market' in locals():
            print("Used existing")
            owned_portfolio=(buy_stocks(market, balance))
        else:
            print("Had to make a new one")
            market=create_market()
            owned_portfolio=(buy_stocks(market, balance))

    elif action == '4':
        if 'owned_portfolio' in locals():
            sell_stocks(owned_portfolio)
        else:
            print('\n'+"----------------------")
            print("Your portfolio is empty")
            print("You have ${:,}".format(balance))

    else:
        print('\n'+"----------------------")
        print("Starting new day...")
        quit()

def main():
    passed_market=create_market()
    insert(passed_market)
    owned_portfolio = {}
    while goto_menu:
        menu(passed_market, owned_portfolio)

main()