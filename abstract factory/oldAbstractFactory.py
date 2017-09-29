"""
Design Pattern: Abstract Factory

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


class mainFactory():
    def run(self):
        print("Welcome to the one and only 4 Da Kids Toy Factory!")
        print("Proudly operating through war time")
        color=input("What color toy are you making? ")
        style = input("What you are you making? ")
        product=None
        # Begin refactor.
        if(style == "flute"):
            if(color == "blue"):
                product= toyFlute("blue")
            elif(color == "red"):
                product= toyFlute("red")
            elif(color == "yellow"):
                product= toyFlute("yellow")
            elif(color == "purple"):
                product= toyFlute("purple")
            elif(color == "grey"):
                product= toyFlute("grey")
            else:
                product=toyFlute("white")
        elif(style == "ball"):
            if(color == "blue"):
                product= toyBall("blue")
            elif(color == "red"):
                product= toyBall("red")
            elif(color == "yellow"):
                product= toyBall("yellow")
            elif(color == "purple"):
                product= toyBall("purple")
            elif(color == "grey"):
                product= toyBall("grey")
            else:
                product= toyBall("white")
        elif(style == "train"):
            if(color == "blue"):
                product= toyTrain("blue")
            elif(color == "red"):
                product= toyTrain("red")
            elif(color == "yellow"):
                product= toyTrain("yellow")
            elif(color == "purple"):
                product= toyTrain("purple")
            elif(color == "grey"):
                product= toyTrain("grey")
            else:
                product= toyTrain("white")
        else:
            if(color == "blue"):
                product= toy("blue")
            elif(color == "red"):
                product= toy("red")
            elif(color == "yellow"):
                product= toy("yellow")
            elif(color == "purple"):
                product= toy("purple")
            elif(color == "grey"):
                product= toy("grey")
            else:
                product= toy("white")
        # End Refactor
        product.play()
        print("Toy quality has been assured. Shutting down")

oldRunnable= mainFactory()
oldRunnable.run()
