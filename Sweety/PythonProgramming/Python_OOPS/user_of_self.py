class City:
    def __init__(self, city_name, city_population):
        self.City_Name = city_name
        self.City_Population = city_population

    def show_city_details(self):
        print("City Name: ", self.City_Name)
        print("City Population: ", self.City_Population)

    @staticmethod
    def square(n):
        print(n**2)

    def addition(self, n1, n2):
        print("add: ", n1 + n2)

obj = City('Mumbai', '5 Cr')
obj.show_city_details()
City.square(5)
obj.addition(10, 20)
