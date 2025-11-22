""""
There are three types of methods :
1. Instance method: when we define any method with self as first parameter then it called instance method.
2. Class method :  when we define method with cls as first param, then it is class method.
                   This method only deals with class variable.
                   @classmethod
                   def test_method(cls):
                       code

3. static method :  when we define method with @staticmethod decorator, it only associated with class name.
                    ->  no need create object to access the class method.
                    @staticmethod
                   def test_method(cls):
                       code
"""

class car:
    car_brand = "Suziki"
    def __init__(self,car_name,car_price):
        self.car_name = car_name
        self.car_price = car_price

    def show_car_name(self):
        print(" Display Car Name :", self.car_name)

    def show_car_price(self):
       print("Display Price :", self.car_price)

    @classmethod
    def car_brand_name(cls):
        print("Show Car Brand Name :",cls.car_brand)

    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact *i
        return fact


obj = car("Swift Dzire","10 Lakhs")
obj.show_car_name()
obj.show_car_price()
obj.car_brand_name()
output = obj.get_factorial(5)
print("Factorial :", output)

"""
 Display Car Name : Swift Dzire
Display Price : 10 Lakhs
Show Car Brand Name : Suziki
Factorial : 120
"""
