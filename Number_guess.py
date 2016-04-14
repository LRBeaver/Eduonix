__author__ = 'lyndsay.beaver'
import random

chosen_number = random.randint(1,100)



while True:
    guess = int(input("What is your guess? (number): "))
    if guess > chosen_number:
        print("You're too high. Try again")
    elif guess < chosen_number:
        print("You're low. Try again")
    else:
        print("Great job. You chose it exactly!")
        break


