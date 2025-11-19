from class_file1 import Animal

#obj = Animal('Shira','Bengal Tiger','Roar')
#obj.show_name()
#obj._show_bread()
#obj._Animal__show_voice()

'''
Animal name : Shira
Animal bread : Bengal Tiger
Animal Voice : Roar
'''

class Dog(Animal):
    def __init__(self, D_name, D_bread, D_voice ,name, bread, voice):
        super().__init__(name, bread, voice)
        self.Dog_name = D_name
        self._Dog_bread = D_bread
        self.__Dog_voice = D_voice

    def Dog_details(self):
        print("Dog name :", self.Dog_name)
        print("Dog Bread :", self._Dog_bread)
        print("Dog Voice :", self.__Dog_voice)


obj =  Dog('Raja','Germansherpad','Brak','Shira','Bengal Tiger','Roar')
obj.Dog_details()
obj.show_name()
obj._show_bread()
obj._Animal__show_voice()

'''
Dog name : Raja
Dog Bread : Germansherpad
Dog Voice : Brak
Animal name : Shira
Animal bread : Bengal Tiger
Animal Voice : Roar
'''