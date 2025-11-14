"""
Object-Oriented-Programming

class -: Class is the blueprint of the object, where use to define all methods/attribute/variable/properties
Object : Object is any entity through which we can access the properties mention in the class
method: When we define any function inside class then it become method.
Constructor : Constructor initialize the memory for the obj, whenever create obj of the class.
              Constructor will call automatically, when we can create object of the class.

"""

class Car:
    def car_name(self):
        print("TATA")
    def car_price(self):
        print("20 lac")

carobj=Car()
carobj.car_name()
carobj.car_price()