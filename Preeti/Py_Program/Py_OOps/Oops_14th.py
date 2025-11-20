#class
import self


class Car:
# Constructor
    def __init__(self,car_name,car_price):
        print("Welcome")
        self.car_name=car_name  #instant variable
        self.car_price=car_price  #instant variable
#method
    def show_car_name(self):
      print(self.car_name)
    def show_car_price(self):
       print(self.car_price)

#create object
obj=Car('Audi Q3','50lac')
obj.show_car_name()
obj.show_car_price()

print("*"*50)
#create n number of objects
obj2=Car('Defender','1 cr')
obj2.show_car_name()
obj2.show_car_price()











