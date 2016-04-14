__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
import random as rnd

#"{:,}".format(value)

starting = 10000
balance = starting
portfolio = {'DEF': 23, 'HGI': 14}
goto_menu = True

def create_market():
    stocks = ['ABC', 'DEF', 'HGI', 'LMK', 'OMN', 'PQR', 'STU', 'XYZ']
    prices = []

    for x in range(len(stocks)):
        prices.append(rnd.randint(10,20))

    market = dict(zip(stocks, prices))
    print(market)
    return market

def do_math(balance):
    print("Starting with: ${:,}".format(balance))
    print("Calculating...")
    new_balance = balance - 800
    print("You now have this much cash left: ${:,}".format(new_balance))
    return new_balance

def change_holdings(market, balance):
    print("Coming over: ${:,}".format(balance))
    print("Calculating...")
    #stock = 'ABC'
    del market['ABC']
    new_holdings = market
    print("This is new list: ", new_holdings)
    return new_holdings

def check_account(portfolio, balance):
    new_balance = balance
    current_portfolio = portfolio
    print("Your account has: ${:,}".format(new_balance))
    print("Your holdings are: ", current_portfolio)
    #return new_balance

def menu():
    passed_market=create_market()
    print('\n'+"----------------------")
    print(""" Market game - stocks
        [1] Check balance
        [2] Do math
        [3] Change market
        [4] Check holdings
        [-] End the day
        """)

    action = input('What would you like to do?: ')
    if action == '1':
        print('\n'+"----------------------")
        print("You chose to check your balance")
        check_account(passed_market, balance)

    elif action == '2':
        print('\n'+"----------------------")
        print("You chose to do math")
        do_math(balance)

    elif action == '3':
        print('\n'+"----------------------")
        print("You chose to change the market")
        change_holdings(passed_market, balance)

    elif action == '4':
        print('\n'+"----------------------")
        print("You chose to check holdings")
        change_holdings(portfolio, balance)

    else:
        print('\n'+"----------------------")
        print("Quit")
        goto_menu = False
        quit()

def main():
    while goto_menu:
        menu()

main()
