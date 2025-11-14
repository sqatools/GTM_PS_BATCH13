class car:
    car_brand = "TATA"
    def __init__(self, car_name, car_price):
        print("Welcome to car world")
        self.car_name = car_name
        self.car_price = car_price

    def show_car_name(self):
        print("Car name:", self.car_name)

    def show_car_price(self):
        print("Car price:", self.car_price)

obj = car('Honda', '40 Lac')
obj.show_car_name()
obj.show_car_price()
print("-"*100)
obj = car('Toyota', '70 Lac')
obj.show_car_name()
obj.show_car_price()