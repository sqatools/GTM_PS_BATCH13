from operator import concat


class Vehical():
    def __init__(self, vtype, wheels_ct=4, origin='USA'):
        self.vtype = vtype
        self.wheels_ct = wheels_ct
        self.origin = origin
    def acc_vtype(self):
        print("Vehical type is", self.vtype)
    def acc_wheels_ct(self):
        print("Wheels ct is", self.wheels_ct)
    def acc_origin(self):
        print("Origin is", self.origin)
class Car(Vehical):
   # def __init__(self, make, model, year, vtype, wheels_ct, origin):
    def __init__(self, make, model, year, vtype):
        super().__init__(vtype)
        self.make = make
        self.model = model
        self.year = year

    def acc_make(self):
        print("Make is", self.make)

    def acc_model(self):
        print("Model is", self.model)

    def acc_year(self):
        print("Year is", self.year)

class Green_Tech():
    def __init__(self, device_type, power_type):
        ##super().__init__(device_type, power_type)
        self.device_type = device_type
        self.power_type = power_type

    def acc_device_type(self):
        print("Device type is", self.device_type)
    def acc_power_type(self):
        print("Power type is", self.power_type)

class EV(Car, Green_Tech):
    def __init__(self, battery_life, price, availability, make, model, year, vtype, device_type, power_type):
        super().__init__(make, model, year, vtype)
        self.device_type = device_type
        self.power_type = power_type
        self.battery_life = battery_life
        self.price = price
        self.availability = availability
    def acc_battery_life(self):
        print("Battery Life is", self.battery_life)
    def acc_price(self):
        print("Price is", self.price)
    def acc_availability(self):
        print("Availability is", self.availability)

obj2 = EV('90000 Hrs','72000 USD','2026 Q2','TESLA','Y3A','2026','Automobile','Car', 'Battery')
obj2.acc_battery_life()
obj2.acc_price()
obj2.acc_availability()
obj2.acc_make()
obj2.acc_model()
obj2.acc_year()
obj2.acc_vtype()
obj2.acc_wheels_ct()
obj2.acc_origin()
obj2.acc_power_type()
obj2.acc_device_type()