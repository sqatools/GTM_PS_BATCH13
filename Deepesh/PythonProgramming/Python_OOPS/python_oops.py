"""
class:  class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
constructor: constructor initialize the memory for the object, when ever we create object of the class
             ->  constructor will be call automatically, when we can create object of the class.
"""
# class
class Car:
    # constructor
    def __init__(self):
        print("-----Welcome to car class -----")
        # calling method inside the constructor
        self.car_price()
    # Method
    def car_name(self):
        print("TATA Harrier")

    # Method
    def car_price(self):
        print("20 Lac")

# create object
obj = Car()
# calling method with object
obj.car_name()






