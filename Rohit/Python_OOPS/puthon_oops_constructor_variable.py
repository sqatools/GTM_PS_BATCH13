



# class
class car:

    # parametrize constructor
    def __init__(self,car_name,car_price):
        # calling method inside the constructor
        self.car_name = car_name  # instance variable
        self.car_price = car_price  # instance variable

    # Method
    def show_car_name(self):
            print("car name:",self.car_name)

    # Method
    def show_car_price(self):
        print("car price :",self.car_price)

# create object
obj = car('Swift Dzire','10 Lac')
# calling method with object
obj.show_car_name()
obj.show_car_price()

#car name: Swift Dzire
#car price : 10 Lac

print("-"*50)
obj1 = car('TATA','25 Lac')
obj1.show_car_name()
obj1.show_car_price()

#car name: TATA
#car price : 25 Lac