class car:
    car_brand = "TATA"

    def __init__(self, car_name, car_price):
        self.car_name = car_name
        self.car_price =car_price

    def show_car_name(self):
        print(self.car_name)

    def show_car_price(self):
        print(self.car_price)

    @classmethod
    def show_brand_name(cls):
        print (cls.car_brand)

    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range (num,0,-1):
            fact = fact*1
        return fact

obj = car("Audi", "2cr")
obj.show_car_name()
obj.show_car_price()

car.car_brand
val = car.get_factorial(5)
print ("factorial no", val)