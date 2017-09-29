"""
Design Pattern: Factory Method

The factory method is a means of managing object creation, making it a
creational design pattern. It focuses on having a means to simply create
instances of specific takes on a general object. If you have to create objects
that implement an interface or abstract class, it can be helpful to encapsulate
the instantiation in a "Factory Method" (that is, to say, have a method which
builds and returns the class, like a factory)
"""

# The scenario: 4 Da Kids Toys
'''
You are programming an assembly line for 4 Da Kids Toys. You make a few
different types of toys on the same machines, but you want to easily control
what toy gets built on which machine. The machine simply requests you tell it
what to build and it will make it, but your supervisor has complained recently
that the code base is cluttered and needs refactoring.
'''

# The existing code

class toy():
    def play(self):
        print("You play with the toy")

class toyTrain(toy):
    def play(self):
        print("You play with the train. Choo choo!")


class toyFlute(toy):
    def play(self):
        print("You play with the flute. Toot toot!")

class toyBall(toy):
    def play(self):
        print("You play with the ball. Bouncy bouncy")


class oldMainClass():
    def run(self):
        print("Welcome to 4 Da Kids Toys")
        startupSequence()
        while( not endOfDay):
            

    def startupSequence():
        print("Doing routine startup tasks")
        print("Startup complete, ready to assemble")

oldRunnable= oldMainClass()
oldRunnable.run()
