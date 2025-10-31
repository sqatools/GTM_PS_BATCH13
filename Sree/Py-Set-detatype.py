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
s3={9,7.7,(4,5,6),'method',False}
s3.discard((4,5,6))
print(s3)
s3={9,7.7,(4,5,6),'method',False}  ### remove non-existing value
s3.discard(10)
print(s3)
print('- '*40)
##############################################
##Combine two sets
s1={'a','b','c'}
s2={0,9,10}
s1.update(s2)
print(s1)
s3=s1.union(s2)
print(s3)
s3=s2.union(s1)
print(s3)
print('- '*40)
### difference method :  this method return the difference values from one set to another################

s1={'a','b','c',9}
s2={0,9,10,'a','b'}
s3=s2.difference(s1)
print(s3)
print('- '*40)
######### symmetric difference method :  this method return the difference values from both sets#############
s1={'a','b','c',9}
s2={0,9,10,'a','b'}
x=s1.symmetric_difference(s2)
print(x)
# intersection method :  this method return the common values from both sets
s1={'a','b','c',9}
s2={0,9,10,'a','b'}
Y=s1.intersection(s2)
print('intersection values:', Y)
print('- '*40)
# conversion from set to list
#####################################
