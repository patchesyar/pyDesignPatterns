"""
Design Pattern: Factory Method (Refactored)

The factory method is a means of managing object creation, making it a
creational design pattern. It focuses on having a means to simply create
instances of specific takes on a general object. If you have to create objects
that implement an interface or abstract class, it can be helpful to encapsulate
the instantiation in a "Factory Method" (that is, to say, have a method which
builds and returns the class, like a factory)
"""



class toy():
    def play(self):
        print("You play with the toy")

class toyTrain():
    def play(self):
        print("You play with the train. Choo choo!")


class toyFlute():
    def play(self):
        print("You play with the flute. Toot toot!")

class toyBall():
    def play(self):
        print("You play with the ball. Bouncy bouncy")


class newMainClass():

    # New Method: Factory

    def factory(self, toyType):
        if (toyType=="ball"):
            toy= toyBall()

        elif (toyType=="flute"):
            toy= toyFlute()
            
        elif (toyType=="train"):
            toy= toyTrain()

        else:
            toy=toy()

        return toy

    def run(self):
        print("Welcome to 4 Da Kids Toys")
        toyType= input("Select the type of toy to make: ")
        toy=None
        # begin refactor
        toy=self.factory(toyType)
        # end refactor
        toy.play()
        print("Toy quality has been assured. Shutting down")



newRunnable= newMainClass()
newRunnable.run()

# What changed and why did we do it?

'''
The name of the game with the factory method is encapsulation. By creating a
single method responsible for creating all objects which implement the same
interface, we are able to encapsulate the functionality. What this means is
that if we look to extend the function further, we do not clutter up, say, the
main function with another set of lines for an if/ switch statement. We instead
isolate the function in a method which is solely devoted to managing object
creation. Factory methods may seem excessive (and sometimes perhaps are), but
in large programs where either the containing function is already long or
cluttered, or when you have a large number of objects to account for it can
significantly improve code readability.

Furthermore, cases of Factory Method may lead to the use of other patterns,
especially the Abstract Factory, which directly extends the factory concept.
"""
