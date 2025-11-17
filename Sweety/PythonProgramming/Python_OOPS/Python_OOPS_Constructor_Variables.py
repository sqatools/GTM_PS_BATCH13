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
class Tea:
    tea_brand = "Brooke Bond"

    #parameterized constructor
    def __init__(self, tea_name, tea_price):
        print("-------Welcome to tea class________")
        # calling method inside the constructor
        self.tea_name = tea_name
        self.tea_price = tea_price

    # Method
    def show_tea_name(self):
        print("Tea Name:", self.tea_name)

    # Method
    def show_tea_price(self):
        print("Tea Price:", self.tea_price)


# create object
obj1 = Tea('Red Label', '50')
# calling method with object
obj1.show_tea_name()
obj1.show_tea_price()

print(obj1.tea_brand)

print("_"*50)
obj2 = Tea('Tata Tea gold', '50')
obj2.show_tea_name()
obj2.show_tea_price()


