class City:
    def __init__(self, city_name, city_population):
        self.city_name = city_name
        self.city_population = city_population

    @staticmethod
    def square(n):
        print(n**2)


    def show_city_details(self):
        print("city name :", self.city_name)
        print("city population :", self.city_population)


    def addition(self, n1, n2):
        print("add :", n1+n2)


obj = City("Mumbai", "5 Cr")
City.square(5)
City.addition(obj, n1=1, n2=20)
#obj.addition(n1=40, n2=50)

