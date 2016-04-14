__author__ = 'lyndsay.beaver'

def sell_stocks(passed_portfolio,balance):
    sold_ticker=input("What stock would you like to sell?: ")
    if sold_ticker in passed_portfolio:
        shares_to_sell=input("How many shares would you like to sell?: ")
        if shares_to_sell <= owned_shares:
            print("Selling x shares:")


def main():
    passed_market=create_market()
    print(""" Market game - stocks

        [1] Check the market
""")

action = input('What would you like to do?: ')

if action == 1:
    print("You chose to sell stocks")
    owned_porfolio={"XYZ", 200}
    passed_portfolio=owned_portfolio
    sell_stocks(owned_porfolio, balance)