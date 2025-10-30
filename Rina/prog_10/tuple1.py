"""
set_a = {5, 8, 99}
set_b = {88, 74, 1}
set_c = set_a.union(set_b)
print("set_c :", set_c)

tup_1 = {5, 4, ('a', 'b', 'c'), ('logo', 'logic'), False}

# print("tup_1 :", tup_1)
for val in tup_1:
    print(val)
"""

tup_1 = (5, 4, ('a', 'b', 'c'), ('logo', 'logic'), False)
for i in range(len(tup_1)):
    print(i, tup_1[i])