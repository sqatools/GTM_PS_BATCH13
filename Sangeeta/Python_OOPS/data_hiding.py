# To achieve data hiding, we have to define variable and method name with single or double underscore or prefix

class Market:
    def __init__(self, mkt_name, mkt_place, mkt_area):
        self.mkt_name = mkt_name
        self.mkt_place = mkt_place
        self.mkt_area = mkt_area

    def show_market(self):
        print("Market Name is :", self.mkt_name)

    def _show_market_place(self):
        print("Market Place :", self.mkt_place)

    def __show_market_area(self):
        print("Market Area :", self.mkt_area)

mkt = Market('Farmers Market', 'Golden Circle','Summit')
mkt.show_market()
mkt._show_market_place()
mkt._Market__show_market_area()
