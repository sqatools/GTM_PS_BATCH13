class Car:
    car_brand = "BMW"
    def __init__(self, car_name, car_type):
        print("Initializing Car")
        self.car_name = car_name
        self.car_type = car_type

    def show_name(self):
        print("The Car Name is:",self.car_name)

    def show_type(self):
        print("The Car Type is:",self.car_type)

    def show_brand(cls):
        print("The Car Brand is:",cls.car_brand)

obj = Car('X6','SUV')
obj.show_brand()
obj.show_name()
obj.show_type()