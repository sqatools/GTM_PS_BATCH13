
class: class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
constructor: constructor initialize the memory for the object, when ever we create object of the class
             ->  constructor will be call automatically, when we can create object of the class


 #####
class mobile:
    # constructor
    def __init__(self):
        print("-----Welcome to mobile class -----")
        # calling method inside the constructor
        self.mobile_price()
    # Method
    def mobile_name(self):
        print("Motorola")

    # Method
    def mobile_price(self):
        print("10 tho")

# create object
obj = mobile()
# calling method with object
obj.mobile_name()
