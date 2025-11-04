dict1 = {'a': [1,2,3], 'b': [4,5,6],'c': [7,8,9]}
dict2 = {}
for k, v in dict1.items():
    dict2[k] = sum(v)
print("Output", dict2)

print("*"*50)
dict2.update(dict1)
print("Output", dict2)
dict2 = {'d' : [1,2,3], 'e' : [4,5,6]}
dict2.update(dict1)
print("Output", dict2)

print("*"*50)
dict4 = {'1': ['a', 'b'], '2': ['c', 'd']}
print("Output", dict4)
dict4['3'] = ['e', 'f']
print("Output", dict4)
dict4.pop('2')
print(dict4)
for k, v in dict4.items():
    print(k, v, end=" ")
print("\n"*2)

del dict1['b']
print(dict1['a'])
##print(dict1['b'])
print(dict1['c'])


