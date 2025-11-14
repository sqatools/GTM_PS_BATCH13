
# There are 2 types of constructor - Default and Paramterized constructor
#Default - def __init__()
#  pass
# Parameterized constructor
#     def__init__(param1, param2):
        #pass


class Food:
    def __init__(self, fruit_name, veggie_name):
        print("-------Welcome to the market------")
        self.fruit_name = fruit_name
        self.veggie_name= veggie_name
    def show_fruit_name(self):
        print("Fruit name : ",self.fruit_name)
    def show_veggie_name(self):
        print("Veggie Name : ", self.veggie_name)

fd = Food('Avocado', 'Potato')
fd.show_fruit_name()
fd.show_veggie_name()
fd1 = Food('Kiwi', 'Okra')
fd.show_veggie_name()
fd.show_veggie_name()
fd2 = Food('Orange', 'Beans')
fd.show_veggie_name()