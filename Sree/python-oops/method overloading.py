"""
method overloading: Method overloading is not supported in python
                       -> When one class have 2 method with same but different parameter, then it is called method overloading.
                       -> but in python if we defined 2 method with same, name then latest defined method will get priority.
"""

class math2:
    def __init__(self, x, y):

        self.x=x
        self.y=y
    def subtraction(self):
        print('sub:',self.x-self.y)
    def multiplication(self,v1,v2):
        print('mul:',v1*v2)
    def greeting(self,name,msg):
        print(f"{name}, {msg}")
    def greeting(self,msg):
        print(f"{msg}")
obj=math2(x=20,y=10)
obj.subtraction()
obj.multiplication(10,5)
obj.greeting('Happy birthday')