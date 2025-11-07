dict_x={'a':4,'b':3,'c':2,'d':1}
print("Items:")
print(dict_x.items())
print("Keys:")
print(dict_x.keys())
print("Values:")
print(dict_x.values())
result1 = dict(sorted(dict_x.items()))
print("sorted with keys:",result1)
result2 = dict(sorted(dict_x.items(), key=lambda item: item[0]))
print("sorted with values:",result2)

#******
 #programt to practice

fruit_price={ "Apple": 50, "Mango": 30, "Banana": 10, "Watermelon":25}
fruit_purchased={"Apple": 10, "Mango":5,"Banana":12,"Watermelon":2}

#Calculate total bill
total_bill = 0
for fruit,price in fruit_price.items():
    f_purchase = fruit_purchased[fruit]
    fruit_bill =price*f_purchase
    total_bill = total_bill + fruit_bill


print("Total bill:",total_bill)



