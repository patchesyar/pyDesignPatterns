"""
Design Pattern: Strategy

Strategy is a design pattern that dictates the flow of functionality in your
program, making it a behavioral pattern. Its intent is to help you manage
multiple means of doing one of any number of actions, each of which are equally
viable at the given time. This separates it from the State pattern, which
requires a specific response based on the current state of the program.
"""

# The scenario: Day Traders 'R US training

'''
Day Traders 'R Us is a stock trading site that has tasked you with refactoring
their training software. Rather than relying on the actual market values, the
user can invoke market changes on their own. To help simulate them, the user
can select one of a number of different choices for market trends, including
bear (trending downwards) and bull (trending upwards), as well as high and low
variance versions. The user can, at will, select any of these market trends
and see how they impact a given example stock
'''

import random

class tradersRUs():
    stockValue=20.00 # stock's initial share value: $20.00
    def run(self):
        print("Welcome to Day Traders 'R Us training system")
        print("You have 1 share in a 20 dollar stock")
        print("The following market trends are available:")
        print("1. Simple Bear Market (downward trend)\n2. Simple Bull Market",\
              " (upward trend)\n3. Low variance stagnant market\n4. High ",\
              "variance Bear Market\n5. High variance Bull Market")
        print("Type any other value to exit the program")
        keepSwimming=True
        while(keepSwimming):
            # Begin Refactor
            command=input("input your desired market trend: ")
            if(command=="1"):
                rando=random.uniform(.75,1.05)
                tradersRUs.stockValue*=rando
            elif(command=="2"):
                rando=random.uniform(.95,1.25)
                tradersRUs.stockValue*=rando
            elif(command=="3"):
                rando=random.uniform(.9,1.1)
                tradersRUs.stockValue*=rando
            elif(command=="4"):
                rando=random.uniform(.5,1.1)
                tradersRUs.stockValue*=rando
            elif(command=="5"):
                rando=random.uniform(.9,1.5)
                tradersRUs.stockValue*=rando
            # End Refactor
            else:
                keepSwimming=False
            print("The current value of the stock is %f"%tradersRUs.stockValue)
        print("You have chosen to end the market trend module.")
        print("Thank you and have a nice day!")

oldRunnable=tradersRUs()
oldRunnable.run()
