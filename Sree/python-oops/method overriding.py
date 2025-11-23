"""
Polymorphism : when one method/variable with same name and perform multiple task, then it is called polymorphism.
1. method overriding: When 2 classes are connected to each with inheritance and have method with same name in both the class
                      then child class method will override the parent class method.
"""
class math1:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def addition(self):
        print('addition:',self.n1+self.n2)
    def multiplication(self,v1,v2,v3):
        print('multiply:',v1*v2*v3)
class math2(math1):
    def __init__(self, x, y, n1, n2):
        super().__init__(n1, n2)
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
obj=math2(x=20,y=10,n1=30,n2=5)
obj.addition()
obj.subtraction()
obj.multiplication(10,5)
obj.greeting('Happy birthday')