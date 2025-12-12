"""There are 2 types of constructor
1).  default constructor :
  def __init__(self)
     pass


2)  Parametrize constructor: when we pass parameter to the constructor then it is called parametrize constructor.
  def __init__(self, param1, param2):
     pass

Instance variable - In Python, an instance variable is a variable that is unique to each instance (object) of a class.
This means that every object created from a class will have its own independent copy of these variables,
and changes made to an instance variable in one object will not affect the same instance variable in other objects of the same class.

########## Variables ###########
1). instance variable :  when we define any variable with self  then it is called instance variable
2). class variable:  when we define any variable on class level, then it is called class variable

"""
# class
class Car:
    car_brand = "TATA"

    # parametrize constructor
    def __init__(self, car_name, car_price):
        print("-----Welcome to car class -----")
        # calling method inside the constructor
        self.car_name = car_name   # instance variable - using the self keyword
        self.car_price = car_price # instance variable - using the self keyword
        #once instance variable is defined - it can be used inside the class anywhere

    # Method
    def show_car_name(self):
        print("Car name:", self.car_name)

    # Method
    def show_car_price(self):
        print("Car price:", self.car_price)


# create object - instance 1
obj = Car('Audi Q3', '50 Lac')
# calling method with object
obj.show_car_name()
obj.show_car_price()

#instance- 2
print("_"*50)
obj2 = Car('Defender', '1 Cr')
obj2.show_car_name()
obj2.show_car_price()


print(obj2.car_brand)

print("*"*50)
####################################################################################
class Dog:
    def __init__(self, name, breed):
        self.n = name  # Instance variable, self.n need not be same as self.name - its just a variable
        self.b = breed # Instance variable

#the variable name and method name must not be same
    def bark(self):
        print(f"{self.n} says Woof!")

# Creating instances of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Lucy", "Labrador")

# Accessing instance variables
print(f"Dog 1: {dog1.n}, {dog1.b}") #Dog 1: Buddy, Golden Retriever
print(f"Dog 2: {dog2.n}, {dog2.b}") #Dog 2: Lucy, Labrador

# Modifying an instance variable for one object
dog1.name = "Max"
print(f"Dog 1 (after modification): {dog1.name}, {dog1.b}") #Dog 1 (after modification): Max, Golden Retriever
print(f"Dog 2 (unaffected): {dog2.n}, {dog2.b}") #Dog 2 (unaffected): Lucy, Labrador
