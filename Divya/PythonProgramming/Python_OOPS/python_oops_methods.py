class Car:
#Car variable
    car_brand = "TATA"

#parametrize constructor
def __int__(self,car_name,car_price):
    print("---Welcome to car class--")
    #calling method inside the constructor
    self.car_name = car_name #instance variable

    self.car_price = car_price  #instance variable

    #Method/ instance method
    def show_car_name (self):
        print("The car name is :",self.car_name)
    #Method/ instanace method
    def show_car_price(self):
        print("The car price is :",self.car_price)



    @classmethod
    def show_brand_name(cls):
        print("The brand name is :",cls.brand_name)
    @staticmethod
    def get_factorial(number):
        factorial = 1
        for i in range(number):
            factorial *= i
            return factorial

"""
obj = Car("Defender", "2Cr")
#access class method with object
obj.show_brand_name()
#acces instance method with object
obj.show_car_price()

#access instance method with object
obj.show_car_price()
"""

#Acess class  method

