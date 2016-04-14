__author__ = 'lyndsay.beaver'

def account(balance):
    print(balance)
    #cash_available = 10000
    print('\n'+"----------------------")
    print("You have:", balance)
    print("${:,}".format(balance))
    return balance

def main():
    balance = 10000000
    print(balance)
    print("${:,}".format(balance))
    print("We're in main", account(balance))


main()

#print("Your balance is: ${:,}".format(value))

#"{:,}".format(value)