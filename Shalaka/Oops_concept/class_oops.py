class car:
    def __init__ (self) : #### constructor
        print("Welcome to class")

    #### Method 1
    def my_car(self):
        print("My car is : TATA")

    #### Method 2

    def my_car_price(self):
        print("10 lcas")


#### create object
obj = car()

#### caal the functions/methods
obj.my_car()
obj.my_car_price()



class car_world:

    def __init__(self):  #### constructor
        print("Welcome to car world")

        ### Calling method inside constructor=
        self.car_price()


        #### Method 1
    def car_name(self):
        print("My car is : TATA")

        #### Method 2
    def car_price(self):
        print("10 lcas")

obj1 = car_world()
obj1.car_name()
