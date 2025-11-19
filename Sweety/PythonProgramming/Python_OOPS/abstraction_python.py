"""
When we provide overview information to the user and hide internal structor of the code, then it is called abstraction.
->  when we define a method in one and impliment the same method in child class then it is called abstract method.

"""
from abc import abstractmethod
class Animal:

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def bread(self):
        pass

    @abstractmethod
    def voice(self):
        pass


class Lion(Animal):
    def name(self):
        print("Shera")

    def bread(self):
        print("African Lion")

    def voice(self):
        print("Roar")


class Dog(Animal):
    def name(self):
        print("Tommy")

    def bread(self):
        print("Germen")

    def voice(self):
        print("Bark")


obj = Lion()
obj.name()  # Shera


obj2 = Dog()
obj2.name() # Tommy