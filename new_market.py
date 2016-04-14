__author__ = 'lyndsay.beaver'
import random as rnd

def create_market():
    market= {'ABC':rnd.randint(10,20), 'DEF': rnd.randint(10,20), 'XYZ': rnd.randint(10,20)}
    return market

def check_market(passed_market):
    print(passed_market)

def main():

    main_market = create_market()
    check_market(main_market)

#def main():
    # passed_list inside useTheList is set to what is returned from defineAList
    #useTheList(defineAList())

main()
