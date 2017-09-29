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
        
        simpleBull= simpleBullStrategy()
        simpleBear= simpleBearStrategy()
        stagnant= stagnantStrategy()
        extremeBull= extremeBullStrategy()
        extremeBear= extremeBearStrategy()
        
        while(keepSwimming):
            # Begin Refactor
            command=input("input your desired market trend: ")
            modifier=1
            if(command=="1"):
                modifier= simpleBear.trend()
            elif(command=="2"):
                modifier= simpleBull.trend()
            elif(command=="3"):
                modifier= stagnant.trend()
            elif(command=="4"):
                modifier= extremeBear.trend()
            elif(command=="5"):
                modifier= extremeBull.trend()
            # End Refactor
            else:
                keepSwimming=False
            tradersRUs.stockValue*=modifier
            print("The current value of the stock is %f"%tradersRUs.stockValue)
        print("You have chosen to end the market trend module.")
        print("Thank you and have a nice day!")

class marketStrategy():
    
    def trend(self):
        return random.uniform(self.lowerBound,self.upperBound)

class simpleBearStrategy(marketStrategy):
    def __init__(self):
        self.lowerBound=.75
        self.upperBound=1.05

class simpleBullStrategy(marketStrategy):
    def __init__(self):
        self.lowerBound=.95
        self.upperBound=1.25

class stagnantStrategy(marketStrategy):
    def __init__(self):
        self.lowerBound=.9
        self.upperBound=1.1

class extremeBearStrategy(marketStrategy):
    def __init__(self):
        self.lowerBound=.5
        self.upperBound=1.1

class extremeBullStrategy(marketStrategy):
    def __init__(self):
        self.lowerBound=.9
        self.upperBound=1.5

newRunnable=tradersRUs()
newRunnable.run()


# What changed and why did we do it?

"""
We encapsulated the functionality of determining the market trend modification
into respective classes rather than leaving them in the main method. In doing
this, we are more easily able to identify the specific functionality of each
respective strategy. It may require more individual Lines Of Code, but by
separating the functions into separate classes we are much more able to see
which function is correlated to the overarching strategy and are able to edit
or extend the program with ease.

In this case, with only 5 strategies in place, it may be possible for you to
remember which number selection is which strategy; however, with more options,
as many as 20, this is no longer feasible and separating the strategies into
different classes or methods are much more workable.

Regarding classes vs. methods, in general due to the fact that various
strategies should follow the same general functionality. Repeating the same
method with slightly different variables may seem more efficient but it could
also clutter other classes and doesn't provide the same level of encapsulation,
ultimately reducing code readability. For that reason it is recommended that
classes are used even when just using a different method may suffice.
"""
