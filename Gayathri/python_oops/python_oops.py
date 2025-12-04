
"""
#class - blue print.
e.x iphone 17 - Blue print what all features , memory,camera,storage capacity, default apps-
same with building - blue print of the building

#object - is the final product
final phone - physical product - which we can feel
through the phone we can access all the methods,properties of the class.
unless the product is ready no use of the blue print

class:  class is nothing the blueprint of the object where use define all methods/attribute/variable and properties.
object :  object is an entity through which we can access the properties mentions in the class.
method :  When we define any function inside the class, then it become method.
constructor: when ever we create object of the class, we need to initialize the memory for the object
so that it can store the object reference. this memory initiation is done by constructor automatiaclly
when an obet is cerated fo the class
constructor initialize the memory for the object, when ever we create object of the class
             ->  constructor will be call automatically, when we can create object of the class.


Differnce bewteen function and methods
In Python, both functions and methods are blocks of reusable code designed to perform specific tasks,
but their key difference lies in their association with objects and classes.

Function:
A function is a standalone block of code defined independently, not associated with any particular
object or class.It can be called directly by its name and operates on the data passed to it as arguments.

def greet(name):
    print(f"Hello, {name}!")

greet("Alice") # Calling the function directly

Method:
A method is a function that belongs to an object or a class. It is defined within a class and
is called on an instance of that class (an object) using dot notation.
Methods often operate on the data (attributes) of the object they belong to and can
modify the object's state.

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self): # This is a method
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy")
my_dog.bark() # Calling the method on the 'my_dog' object

Key Differences Summarized:
Association: Functions are independent; methods are associated with classes/objects.
Calling Convention: Functions are called by their name; methods are called using object.method_name().
self Parameter: Methods implicitly receive the instance (object) they are called on as their first argument,
conventionally named self, allowing them to access and manipulate the object's attributes.
Functions do not have this implicit self parameter.
Scope and Data Access: Methods can access and modify the internal state (attributes) of the object they belong to.
Functions typically operate on the data passed to them as arguments and generally do not directly interact with object states
unless an object is explicitly passed as an argument.

class - int, string,tuple,dict,set - all this are class

we used to access the function outside, why need class and define method inside that
- function is like standalone buildings - any one can access
- methods inside the class is liek gated community - where they need persmission to access
- it adds extra security feature
- to access methods inside the class - objects can only do that

what is self in python
self is a the first parameter of a method within a class definition.
It serves as a reference to the current instance of the class on which the method is being called.
class Dog:
    def __init__(self, name, breed):
        self.name = name  # 'self.name' refers to the instance's 'name' attribute
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!") # Accessing the instance's 'name' attribute

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark() # Output: Buddy says Woof!

In this example, self in __init__ and bark refers to the my_dog instance,
allowing the methods to access and use its name and breed attributes.

#theer are 2 types of constructor
1. Default constructor which has only having self
2. paramterized constructor - where we pass the paramters
"""
# class
class Car:
    # constructor
    def __init__(self): #any code defined inside the constructor will be executed first
        print("-----Welcome to car class -----")
        # calling method inside the constructor
        self.car_price()
    # Method
    def car_name(self): #self refers to the current object instance.
        print("TATA Harrier")

    # Method
    def car_price(self):
        print("20 Lac")

# create object for the class
obj = Car()
# calling method with object
obj.car_name()
