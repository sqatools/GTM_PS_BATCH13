class vehicle:
    vehicle_name = "BMW"
    def __init__(self, vehicle_type, vehicle_price):
        print("Welcome to world's best car showroom.")
        self.vehicle_tye = vehicle_type
        self.vehicle_price = vehicle_price

    def show_vehicle_type(self):
        print("Vehicle Type: ", self.vehicle_tye)

    def show_vehicle_price(self):
        print("Vehicle Price: ", self.vehicle_price)

    @staticmethod
    def get_factorial(num):
        fact = 1
        for i in range(num, 0, -1):
            fact = fact *i
        return fact

obj = vehicle("Seven series", "$1000K")
obj.show_vehicle_type()
obj.show_vehicle_price()



