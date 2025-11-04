# write a python program to get number from 1 to 20 and store even value as key and their square as dict value.
# dict2 = {2 :4, 4: 16, 6: 36, 8: 64, 9: 81}
result2 = {}
for i in range(1, 21):
    if i%2 == 0:
        result2[i] = i**2
    else:
        continue
print("result :", result2)

# write a python program to get desire result:
dict1 = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
# output = {'a' : 6, 'b': 15, 'c': 24}
output = {}

for k, v in dict1.items():
    output[k] = sum(v)

print("output :", output)
# output : {'a': 6, 'b': 15, 'c': 24}

