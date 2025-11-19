"""
When we provide overview information to the user and hide internal structor of the code, then it is called abstraction.
->  when we define a method in one and impliment the same method in child class then it is called abstract method.

"""

class Animal():
    def name(self):
        pass

    def bread(self):
        pass

    def voice(self):
        pass

class Tiger(Animal):
    def name(self):
        print("Shira")

    def bread(self):
        print("Bengal")

    def voice(self):
        print("Roar")

    def Tiger_details(self):
        self.name()
        self.bread()
        self.voice()

class Dog(Animal):
    def name(self):
        print("Raja")

    def bread(self):
        print("Germanshepred")

    def voice(self):
        print("Bark")

    def Dog_details(self):
        self.name()
        self.bread()
        self.voice()

obj = Tiger()
obj.Tiger_details()

print("-"*50)

obj = Dog()
obj.Dog_details()

'''
Shira
Bengal
Roar
--------------------------------------------------
Raja
Germanshepred
Bark
'''