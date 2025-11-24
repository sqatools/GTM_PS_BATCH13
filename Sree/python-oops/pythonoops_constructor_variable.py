

""""
class car:
    car_brand="Honda"
# parametrize constructor
    def __init__(self,carname,carprice):   # calling method inside the constructor
         self.carname=carname           # instance variable
         self.carprice=carprice
    def show_carname(self):
         print("carname:",self.carname)
    def show_carprice(self):
         print('carprice:',self.carprice)
## create object
obj=car('Accord',40000)
obj.show_carname()
obj.show_carprice() """
## print("-"*45)"""

class car:
    def carname(self):
        print('honda')
    def carprice(self):
        print(40000)
obj=car()
obj.carname()
obj.carprice()
print('-'*45)
class Van:
    def Van_brand(self):
        print('Subharu')
    def Van_model(self):
        print('Crosstech')
obj=Van()
obj.Van_brand()
obj.Van_model()

print('with constructor',"-"*45)
class van:
    def __init__(self,van_brand,van_model,van_price):
       self.van_brand=van_brand
       self.van_model=van_model
       self.van_price=van_price
    def show_vanbrand(self):
        print(self.van_brand)
    def show_vanmodel(self):
        print(self.van_model)
    def show_vanprice(self):
        print(self.van_price)


obj= van('Honda','civic','55000')
obj.show_vanbrand()
obj.show_vanmodel()
obj.show_vanprice()
print('2nd ex','-'*45)
class motorcycle:
    def __init__(self,motorcycle_name,motorcycle_color,):
        self.motorcycle_name=motorcycle_name
        self.motorcycle_color=motorcycle_color
    def motorcycle(self):
        print(self.motorcycle_name)
    def motorcyclecolor(self):
        print(self.motorcycle_color)
obj=motorcycle('Herohonda','Red')
obj.motorcycle()
obj.motorcyclecolor()










