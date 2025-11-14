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


class diff_car:

    def __init__(self, new_car, new_price):  #### constructor
        print("Welcome to car world")

        ### Calling method inside constructor=
        self.new_car = new_car
        self.new_price = new_price

        #### Method 1

    def show_car(self):
        print(self.new_car)

        #### Method 2

    def show_price(self):
        print(self.new_price)




obj2 = diff_car('Audi','50')
obj2.show_car()
obj2.show_price()
