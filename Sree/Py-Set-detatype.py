set1 = {3, 3.5, 'Hello', (3, 5, 6), True, 3, 3.5, True,False}
print(set1)
print('-'*40)
##############################################
# apply loop on set.
for i in set1:
    print(i)
print('- '*40)
##############################################
# Add method: add data to the set.
s1={2,5,8,9,6}
s1.add(400)
print(s1)
print('- '*40)
##############################################
# remove method: remove any specific data from set
s2={2,5,8,9,6}
s2.remove(9)
print(s2)
print('- '*40)
##############################################
# discard method: this method remove any specific value from set and does not return anything if value is not available