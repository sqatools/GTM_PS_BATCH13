from abc import abstractmethod

class World:
    @abstractmethod
    def nation(self):
        pass

    @abstractmethod
    def language(self):
        pass

class Country(World):
    def nation(self):
        print("Nation :", 'India')

    def language(self):
        print("National language :",'Hindi')

class State(World):
    def nation(self):
        print("Nation :", 'Peru')

    def language(self):
        print("National language :", 'Peruvian')

cntry = Country()
cntry.nation()
cntry.language()

st = State()
st.nation()
st.language()