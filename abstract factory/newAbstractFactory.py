"""
Design Pattern: Abstract Factory (Refactored)

The abstract factory pattern == a creational pattern which directly extends the
standard Factory Method Pattern. The Abstract Factory class sets a framework
containing a factory method, which will be able to provide specialized versions
of objects. The concrete factories which extend the abstract will create
objects that are specialized to meet the needs of the specific concrete factory
specifications, while still meeting the requirements of the created object.
"""

# The scenario: 4 Da Kids Toys- Warring Clans Edition

'''
You are programming an assembly line for 4 Da Kids Toys. You make a few
different types of toys on the same machines, but you want to easily control
what toy gets built on which machine. Recently, a war has broken out between 5
neighboring clans. 4 Da Kids has chosen to stay neutral, and by stay neutral
they mean selling to all 5 clans. Each clan has a single color that all their
toys must be. Your boss has tasked you with ensuring that we can meet this
requirement while still maintaining clean and efficient code.
'''

class toy():
    def __init__(self, color):
        self.color=color
        self.style="Generic"
        
    def play(self):
        print("You play with the %s toy" % self.color)

class toyTrain():

    def __init__(self, color):
        self.color=color
        
    def play(self):
        print("You play with the %s train. Choo choo!" % self.color)


class toyFlute():

    def __init__(self, color):
        self.color=color
        
    def play(self):
        print("You play with the %s flute. Toot toot!" % self.color)

class toyBall():

    def __init__(self, color):
        self.color=color
        
    def play(self):
        print("You play with the %s ball. Bouncy bouncy" % self.color)


class Factory():

    def __init__(self):
        self.color="white"
    def makeFlute(self):
        return toyFlute(self.color)
    def makeTrain(self):
        return toyTrain(self.color)
    def makeBall(self):
        return toyBall(self.color)
    def makeToy(self):
        return toy(self.color)
    def factoryMethod(self, style):
        if(style=="train"):
            return self.makeTrain()
        elif(style=="ball"):
            return self.makeBall()
        elif(style=="flute"):
            return self.makeFlute()
        else:
            return self.makeToy

class blueFactory(Factory):
    def __init__(self):
        self.color="blue"

class redFactory(Factory):
    def __init__(self):
        self.color="red"

class yellowFactory(Factory):
    def __init__(self):
        self.color="yellow"

class purpleFactory(Factory):
    def __init__(self):
        self.color="purple"

class greyFactory(Factory):
    def __init__(self):
        self.color="grey"


class mainClass():
    def run(self):
        print("Welcome to the one and only 4 Da Kids Toy Factory!")
        print("Proudly operating through war time")
        color=input("What color toy are you making? ")
        style = input("What you are you making? ")
        product=None
        # Begin refactor.
        fac= None # factory object
        if(color == "blue"):
            fac= blueFactory()
        elif(color == "red"):
            fac= redFactory()
        elif(color == "yellow"):
            fac= yellowFactory()
        elif(color == "purple"):
            fac= purpleFactory()
        elif(color == "grey"):
            fac= greyFactory()
        else:
            fac= Factory()
        product=fac.factoryMethod(style)
        # End Refactor
        product.play()
        print("Toy quality has been assured. Shutting down")

newRunnable= mainClass()
newRunnable.run()

# What changed and why did we do it?
"""
I'm hopeful that you noticed the 100 line nested if/else block is gone. Because
we have a set of toys which all have the same base functionality (you can play
with them), but are also different in their style or functionality (they are
different colors. In another implementation they may perform differently even
though they have the same base class structure), we are able to use inheritance
to our advantage.

A standard Factory method is useful for encapsulating the creation of one of a
set of objects which inherit functionality. In this case, our Factory method
makes "toys," which could be one of several specific toys. When we want to
account for colors, we can take it a step further and add abstraction to the
factory itself. We make a base factory which has the core functionality of
being able to make toys. We can then make concrete factories based on the
abstract model which makes the same toys, but each concrete factory makes toys
only in one specific color. This makes it easier to extend the functionality.

If you want to add a new toy to your factory, simply add a function to create
the toy, and add that function to the factory method. All the concrete
factories will be able to then create that toy in its specific color. You can
even change the factory method for a concrete factory if a specific factory can
make a certain other concrete factory cannot. It is much more clear and concise
to use this method when comparing to nested if statements
"""
