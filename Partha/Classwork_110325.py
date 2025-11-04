from pprint import pprint
company = {
    'branch' : [
                    {'name': 'Head Office', 'city' : 'New York', 'code' : '001'},
                    {'name': 'Branch Office', 'city' : 'New Orleans', 'code' : '002'}
               ],
'department' : [
                    {'name': 'Finance', 'manager' : 'Richard', 'code' : 'Fin'},
                    {'name': 'Facilities', 'manager' : 'James', 'code' : 'Fac'}
               ]
    }
pprint(company['branch'][1]['city'])
pprint(company)

print('*'*100)


fruit_price = {"Apple": 50, "Banana": 100, "Pear": 120}
fruit_purchased = {"Apple": 3, "Banana": 6, "Pear": 2}
total_price = 0
for fruit, price in fruit_price.items():
    f_quantity = fruit_purchased[fruit]
    print(fruit, ":", price, ":", f_quantity, ":" , price*f_quantity)
    total_price += price * fruit_purchased[fruit]
print("Total Cost", total_price)