n = "_"
print(n*50)

print("Numbers data tpes - Integer, Float, Complex")
print("Integer / float data types")
a = 458
b = 985.4589654
c = 78.5j
print("Value of a:", a, type(a))
print("Value of b:", b, type(b))
print("Value of c:", c, type(c))
print(" ")
print(n*50)
print(" ")

print("Sequential data types - String")
st1 = 'Sequential'
st2 = "Datatype"
st3 = '''Python is a high-level, interpreted, object-oriented programming language known for its clear syntax
 and readability. 
 Created by Guido van Rossum and first released in 1991, its design philosophy emphasizes code readability, 
 making it popular for both beginners and experienced developers. 
'''
print("Value of st1", st1, type(st1))
print("Value of st2:", st2, type(st2))
print("value of st3:",st3, type(st3))
print(" ")
print(n*50)
print(" ")

print("Sequential data type - List ")
list1 = [77, 19.23, 'Hello', [8, 4],(3, 9),{'a': 125}, {45, 67}, True]
print(list1, type(list1))
print("Add a number with append command")
list1.append(100)
print(list1)
print(" ")
print(n*50)
print(" ")

print("Sequential data type - Tuple")
tup1 = (2011, 15.5, 'Hey there', [8, 4],(3, 9),{'b': 567}, {45, 67}, False)
print(tup1, type(tup1))
print(tup1[3])
print(tup1[4][1])
print(" ")
print(n*50)
print(" ")

print("Dictionary data type")
dict1 = {'a':123, 'b': 45.6, 911: 789, 'd': 'Thankyou', 'f' : 5+15j, 5: [8, 9], 't': True}
print(dict1, type(dict1))
print(dict1['b'])
print(dict1['f'])
user_info = {'name': 'Ash', 'height': 5.8, 'color': 'Wheatish', 'phone': 7894561234}
print(user_info)
print(user_info['phone'])
print(" ")
print(n*50)
print(" ")

print("Set data type")
set1 = {'addie', 45.3, True, 'hello', (4, 7, 9)}
print(set1, type(set1))
print(set1)
print(" ")
print(n*50)
print(" ")

print("Boolean data type")
var1 = True
var2 = False
print (var1, type(var1))



