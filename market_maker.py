__author__ = 'lyndsay.beaver'
import sqlite3 as sq1
import random as rnd


#"{:,}".format(value)

starting = 10000
balance = starting

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
    print("Number of stocks: ", len(market))
    database1 = sq1.connect('stocks' + str(rnd.randint(1,20)) + '.db')
    db1_cursor = database1.cursor()

    db1_cursor.execute('CREATE TABLE stocks(ticker TEXT, prices TEXT, current TEXT)')

    list = market.keys()
    for i in list:
        tmp1 = i
        tmp2 = market[i]
        tmp3 = 0

        #print(tmp1)
        #print(tmp2)
        #print(tmp3)
        db1_cursor.execute('INSERT INTO stocks VALUES(?,?, ?)', (tmp1, tmp2, tmp3))


    database1.commit()
    db1_cursor.close()
    database1.close()

def check_market(passed_market):
    print(passed_market)

def buy_stocks(passed_market, balance):
    #print(balance)
    #cash_available = 10000
    print('\n'+"----------------------")
    print("You have ${:,}".format(balance))
    print(passed_market)
    choice = input('What stock do you want to buy?: ')
    print('The price of ' + choice + ' is: ', passed_market[choice])
    print('\n'+"----------------------")
    shares = input('How many shares do you want?: ')
    cost = int(shares) * int(passed_market[choice])
    owned_portfolio={choice:cost}
    print("This transaction will cost: ${:,}".format(cost))
    returned_balance=balance-cost
    print("You now have this much cash left: ${:,}".format(returned_balance))
    return (owned_portfolio, returned_balance)


def sell_stocks(passed_portfolio,balance):
    print('\n'+"----------------------")
    sold_ticker=input("What stock would you like to sell?: ")
    if sold_ticker in passed_portfolio:
        print('\n'+"----------------------")
        shares_to_sell=input("How many shares would you like to sell?: ")
        if shares_to_sell <= owned_shares:
            print("Selling x shares:")


def menu():
    passed_market=create_market()

    print('\n'+"----------------------")
    print(""" Market game - stocks
        [0] Create market
        [1] Check the market
        [2] Check your portfolio
        [3] Buy stocks
        [4] Sell stocks
        [5] End the day
        """)

#"{:,}".format(value)

    action = input('What would you like to do?: ')
    if action == '0':
        print('\n'+"----------------------")
        print('\n'+"Creating Market DB")
        insert(passed_market)
    elif action == '1':
        print('\n'+"----------------------")
        print('\n'+"You chose to check the market")
        check_market(passed_market)
        main()
    elif action == '2':
        print('\n'+"----------------------")
        print("You chose to check your portfolio")
        if 'returned_balances' in locals():
            current_balance=returned_balance
        else:
            current_balance = balance
        if 'returned_balances' in locals():
            current_balance=returned_balance
        else:
            print('Portfolio: ', owned_portfolio)
        print('Cash: ${:,}'.format(current_balance))
        main()
    elif action == '3':
        print('\n'+"----------------------")
        print("You chose to buy stocks")
        returned_portfolio=(buy_stocks(passed_market, balance))
        print("Your portfolio:", returned_portfolio)
        main()
    elif action == '4':
        print('\n'+"----------------------")
        print("You chose to sell stocks")
        main()
    else:
        print('\n'+"----------------------")
        print("Starting new day...")
        quit()

def main():
    while goto_menu:
        menu()

main()