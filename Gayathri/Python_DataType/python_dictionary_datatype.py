#13-Oct-25
#################################### dictionary ###########################
"""
Properties:
->  Dict is mutable datatype, we can modify any point of time.
->  Dict contains data in curly braces in keys value pair e.g.   {key : value}, {'a': 123}
->  Dict contains unique keys, duplicate keys are not allowed.
     {'a': 123, 'b': 456, 'a': 789}
     if we mention the duplicate then it will only consider the latest defined value
     it means it will consider a = 789

->  Only immutable data can be key in the dictionary e.g. int, float, complex,  string, tuple, boolean
   not allowed as key e.g. list, dict, set - these are mutable data type
   e.g.
   {1 : 'Python',
    4.5 : [5, 7, 8],
    5+60j : {'a': 345},
    'Python' : (5, 7, 9),
    True : {4, 7, 9, 1, 2},
    (4, 7, 8) :  {'a': 678}
    }

-> Dict value can contain any types of data. e.g.  int, float, string, list, complex, tuple, set, boolean.
-> Dict does not follow indexing.

-> Dict follow LIFO (LAST IN FIRST OUT) concept
"""

dict1 = {'a': 123, 'b': 567, 'c': 789,'a':889} #duplicate value for a
print(dict1, type(dict1))

# {'a': 889, 'b': 567, 'c': 789} <class 'dict'>

# Get data from dict
print(dict1['a'])
# 889


user_details = {
    "name": "Rahul",
    "age": 25,
    "DOB": "1/02/2000",
    "phone": 78979798789,

}

print("Dict user details are :",user_details)  # {'name': 'Rahul', 'age': 25, 'DOB': '1/02/2000', 'phone': 78979798789}
print(user_details['phone'])  # 78979798789

# Add new detail to dict
user_details["email"] = "rahul1234@gmail.com"
print("Newly added details are :",user_details)
#{'name': 'Rahul', 'age': 25, 'DOB': '1/02/2000', 'phone': 78979798789, 'email': 'rahul1234@gmail.com'}

result = user_details.popitem()
print("Deleted item is :",result)  # ('email', 'rahul1234@gmail.com')
print("latest user details are :",user_details) #{'name': 'Rahul', 'age': 25, 'DOB': '1/02/2000', 'phone': 78979798789}

dict3 = {1: 'Python',
         4.5: [5, 7, 8],
         5 + 60j: {'a': 345},
         'Python': (5, 7, 9),
         True: {4, 7, 9, 1, 2},
         (4, 7, 8): {'a': 678},
         100: 5000,
         }

print(dict3[4.5])  # [5, 7, 8]
print(dict3[100])  # 5000

print("_" * 40)