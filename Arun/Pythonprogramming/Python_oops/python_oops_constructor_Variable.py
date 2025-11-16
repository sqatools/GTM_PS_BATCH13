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

class mobile:
    mobile_brand = "Motorola"


    def __init__(self, mobile_name, mobile_price):
        print("-----Welcome to mobile class -----")

        self.mobile_name = mobile_name
        self.mobile_price = mobile_price


    def show_mobile_name(self):
        print("mobile name:", self.mobile_name)

    # Method
    def show_mobile_price(self):
        print("mobile price:", self.mobile_price)


obj = mobile('Edge 50', '15 tho')

obj.show_mobile_name()
obj.show_mobile_price()


print("_"*50)
obj2 = mobile('Pro 60', '20 tho')
obj2.show_mobile_name()
obj2.show_mobile_price()


print(obj2.mobile_brand)





