class car:
    car_brand = "TATA"
    def __init__(self, car_name, car_price, car_color):
        print("Welcome to car world")
        self.car_name = car_name
        self.car_price = car_price
        self.car_color = car_color

    def show_car_name(self):
        print("Car name:", self.car_name)

    def show_car_price(self):
        print("Car price:", self.car_price)

    def show_car_color(self):
        print("Car color:", self.car_color)

obj = car('Honda', '40 Lac', 'Green')
obj.show_car_name()
obj.show_car_price()
obj.show_car_color()
print("-"*100)
obj = car('Toyota', '70 Lac', 'Red')
obj.show_car_name()
obj.show_car_price()
obj.show_car_color()
print("-"*100)
obj = car('tesla', '30 Lac', 'White')
obj.show_car_name()
obj.show_car_price()
obj.show_car_color()