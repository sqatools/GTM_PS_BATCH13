class animal :
    def name (self):
     pass

    def voice (self):
     pass

    def breed (self):
     pass

class lion(animal):

    def name(self):
        print("lion")

    def voice(self):
        print("Roar")

    def breed(self):
        print("Indian")

obj = lion()

obj.name()
obj.breed()
obj.voice()
