"""
When we provide overview information to the external user and hide internal structor of the code, then it is called abstraction.
->  when we define a method in one and impliment the same method in child class then it is called abstract method.
"""
class Animal:
    def name(self):   #pass is useful because:It avoids syntax errors in empty functions or classes.

                                #It helps create abstract-like base classes.It allows method definitions to exist even without functionali
        pass
    def bread(self):
        pass
    def age(self):
        pass
class Lion(Animal):
    def name(self):
        print('lion')
    def bread(self):
        print('West African lion')
    def age(self):
        print('20months')
obj=Lion()
obj.name()
obj.bread()
obj.age()