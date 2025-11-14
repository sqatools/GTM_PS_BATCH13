

class Car:
    def __init__(self):
        print("-------Welcome to car class------")
        self.car_price()
    def car_name(self):
        print("Tata Motors")
    def car_price(self):
        print("Rs.20 lac")

obj = Car()
obj.car_name() #calling the method