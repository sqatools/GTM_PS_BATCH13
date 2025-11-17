print('1). Python oops program to create a class with the constructor.')

class school:
    school_name = ("Sarawati")

    def __init__(self):
        print("My favourite subject")

    def my_fav_sub(self):
        print("History")

obj= school()
obj.my_fav_sub()


print("2). Python oops program to create a class with an instance variable.")

class fav_sub:
    def __init__(self):
        self.sub = "History"

objsub = fav_sub()
print (objsub.sub)


print("3). Python oops program to create a class with Instance methods.")

class car :
    def __init__(self, car_name, car_price):
        self.car_name = car_name     #### instance vairable
        self.car_price = car_price   #### instance vairable

    def show_car(self):
        print(self.car_name)

    def show_car_price(self):
        print(self.car_price)

obj2 = car ("Audi", "3 cr")
obj2.show_car()
obj2.show_car_price()



print("4). Python oops program to create a class with class variables.")

class fav_food:
    food = "Idali"

print(fav_food.food)