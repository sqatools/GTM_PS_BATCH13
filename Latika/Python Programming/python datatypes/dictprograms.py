from pprint import pprint
print("Program 1 :")
School ={
        'Teacher':
            {
                'English':[
                    {'name':'sania','email':'sania.p@gmail.com','phone':1234567890},
                ],

                    'Maths': [
                        {'name':'preeti','email':'preeti.p@gmail.com','phone':1234567890},
                ],
            },
        'Student':
            {
                '10th':[
                    {'name':'jay','email':'jay.p@gmail.com','phone':1234567890}
                ],
                '11th':[
                    {'name':'shanaya','email':'sh.p@gmail.com','phone':1234567890}
                ],
            },
        'Admin':{
            'account':[],
            'admission':[]
            }
        }
pprint(School)
print()
pprint(School['Student']['10th'])

###################################################program 2##########################################

print()
fruit_price=    {
                "Apple":50,
                "Banana":100,
                "Mango":120,
                "Muskmelon":80
                }
fruit_purchased={
"Apple":50,
                "Banana":5,
                "Mango":10,
                "Muskmelon":2,
                "Apple":4
                }
total_bill=0

for fruit,price in fruit_price.items():
    f_purchased=fruit_purchased[fruit]
    fruit_bill=price*f_purchased
    total_bill=total_bill+fruit_bill

    print(fruit,":",price,":",f_purchased,":",total_bill)
print(total_bill)

print()

for fruit,purchase in fruit_purchased.items():
    f_price=fruit_price[fruit]
    fruit_bill=f_price*purchase
    total_bill1=total_bill1+fruit_bill

    print(fruit,"-",f_price,"-",purchase,"-",fruit_bill)

print(fruit_bill)

