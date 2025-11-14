


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
obj.show_carprice()
