from abc import abstractmethod

class animal:
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def color(self):
        pass

    @abstractmethod
    def breed(self):
        pass

class Dog(animal):
    def name(self):
        print("Nicco")

    def color(self):
        print("Black")

    def breed(self):
        print("German")



obj = Dog()
obj.name()
obj.breed()

