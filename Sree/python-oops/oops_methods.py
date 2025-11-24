"""
class:  class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
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


########## Variables ###########
1). instance variable :  when we define any variable with self  then it is called instance variable
2). class variable:  when we define any variable on class level, then it is called class variable

# self : self is nothing but the instance of the current of class being created.


"""
# class
class Car:
    # class variable
    car_brand = "TATA"

    # parametrize constructor
    def __init__(self, car_name, car_price):
        print("-----Welcome to car class -----")
        # calling method inside the constructor
        self.car_name = car_name   # instance variable
        self.car_price = car_price # instance variable

    # Method/instance method
    def show_car_name(self):
        print("Car name:", self.car_name)

    # Method/instance method
    def show_car_price(self):
        print("Car price:", self.car_price)

    @classmethod
    def show_brand_name(cls):
        print("Show car brand :", cls.car_brand)

    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact *i
        return fact


"""
obj = Car("Defender", "2 Cr")
# access class method with object
obj.show_brand_name()
# access instance method with object.
obj.show_car_price()
# access static method with object.
output = obj.get_factorial(5)
print("Factorial :", output)
"""

##################
# Access class method and static method with class name without creating the object
Car.show_brand_name()
val = Car.get_factorial(6)
print("Factorial of 6 :", val)