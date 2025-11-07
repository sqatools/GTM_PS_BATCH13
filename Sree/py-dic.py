d={'a':85,'c':100,'d':200}
print(d)
print('-'*40)
###########################################
# Add new key to dictionary
d['b']=20
d['e']=77
print(d)
print('-'*40)
###########################################
# Apply loop on dictionary
for k,v in d.items():
   print(k,":", v)
print('-'*40)
###########################################
# write a python program to create a dictionary from given string.
s="Today is Friday"
x = s.split()
print(x)
dic={}
for i in x:
    val=i[0]
    dic[val]=i
    print(dic)
"""s = "Today is  Friday"
x = s.split()  # automatically handles any amount of whitespace
dic = {i[0]: i for i in x}
print(dic)"""
print('-'*40)
###########################################
# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
# dict2 = {2 :4, 4: 16, 6: 36, 8: 64, 9: 81}
dic2 = {}

for i in range(1, 21):
    if i%2 == 0:
        dic2[i] = i**2
    else:
        continue

print(dic2)
print('-'*40)
###########################################
## write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# output = {'a' : 6, 'b': 15, 'c': 24}
output={}
for k,v in dict1.items():
    output[k]=sum(v)
    print(output)
print('-'*40)
###########################################Get data from dictionary
from pprint import pprint
School={
    'Teacher':{
        'Math':[
            {'Name': 'Ram','Email':'Ram@gmail.com','phone': 987654100},
            {'Name': 'Sham','Email':'Sham@gmail.com','phone': 987654100}
        ],
        'English':[
        {'Name': 'Kash','Email':'Kash@gmail.com','phone':9876541}
        ]
    },
    'Students':{
        '9th class': [
           {'Name': 'Sita','Email':'Sita@gmail.com','phone': 9876541}
        ],
        '5th class':[],
    },
    'Admin':{
        'Front office':[
           {'Name': 'Clair','Email':'Clair@gmail.com','phone': 9876541}
        ],
    }

}
pprint(School)


