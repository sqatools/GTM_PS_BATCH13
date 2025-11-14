
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


#################### Constructor ######################
"""
class dwijesh: #creating class

    def __init__(self,a,b): #cresting constructor
        print("welcome to the world")
        self.a=car()   #instance variable
        self.b=bike()   #instance variable


    def car(self): #creating method
        print("its a car")

    def bike(self):
        print("its a bike")

obj=dwijesh()

"""

#abc