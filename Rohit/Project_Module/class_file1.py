class Animal():
    def __init__(self, name, bread, voice):
        self.name = name
        self._bread = bread
        self.__voice = voice

    def show_name(self):
        print("Animal name :", self.name)

    def _show_bread(self):
        print("Animal bread :", self._bread)

    def __show_voice(self):
        print("Animal Voice :", self.__voice)





