"""
class:  class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
constructor: constructor initialize the memory for the object, when ever we create object of the class
             ->  constructor will be call automatically, when we can create object of the class.


There are 2 types of constructor
1).  default constructor :
  def __init__(self)
     pass


2)  Parametrize constructor: when we pass parameter to the constructor then it is called parametrize constructor.
  def __init__(self, param1, param2):
     pass

########## Variables ###########
1). instance variable :  when we define any variable with self  then it is called instance variable
2). class variable:  when we define any variable on class level, then it is called class variable

"""

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