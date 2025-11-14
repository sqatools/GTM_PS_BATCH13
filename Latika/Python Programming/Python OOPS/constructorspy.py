"""
Object-Oriented-Programming

class -: Class is the blueprint of the object, where use to define all methods/attribute/variable/properties
Object : Object is any entity through which we can access the properties mention in the class
method: When we define any function inside class then it become method.
Constructor : Constructor initialize the memory for the obj, whenever create obj of the class.
              Constructor will call automatically, when we can create object of the class.
Variables :
            1. Instance Variable : When we define any variable with self then it is called instance variable.
            2. Class Variable : When we define any variable on class level, then it is called class variable.
"""
class school:

    def __init__(self):
        self.school_name()

    def school_add(self):
            print("Mumbai")

    def school_name(self):
        print("New High School")

schobj=school()
schobj.school_name()








