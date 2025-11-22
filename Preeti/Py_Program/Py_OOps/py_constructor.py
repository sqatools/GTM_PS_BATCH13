
# class
class Car:
    car_brand = "TATA"

    # parametrize constructor
    def __init__(self, car_name, car_price):
        print("-----Welcome to car class -----")
        # calling method inside the constructor
        self.car_name = car_name   # instance variable
        self.car_price = car_price # instance variable

    # Method
    def show_car_name(self):
        print("Car name:", self.car_name)

    # Method
    def show_car_price(self):
        print("Car price:", self.car_price)


# create object
obj = Car('Audi Q3', '50 Lac')
# calling method with object
obj.show_car_name()
obj.show_car_price()


print("_"*50)
obj2 = Car('Defender', '1 Cr')
obj2.show_car_name()
obj2.show_car_price()


print(obj2.car_brand)