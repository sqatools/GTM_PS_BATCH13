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


class my_cars:

    ##### parametrize constructor
    def __init__ (self, new_name, new_price):
        print("My cars")
        self.new_cars = new_name
        self.new_price= new_price

    def owner_name(self):
        print(self.new_cars)

    def owner_price(self):
        print(self.new_price)

obj3 = my_cars('audi','3cr')
obj3.owner_name()
obj3.owner_price()
