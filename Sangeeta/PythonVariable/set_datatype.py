# Properties:
# ->  Set is mutable data type, we can modify any point of time.
# ->  Set only store unique values, duplicate data is not allowed.
# ->  Set store values in random order.
# ->  Set store values in curly braces. e.g. {6, 8, 9, 2, 5, 6}
# ->  Only immutable data type are allowed as member e.g. int. float, string, tuple, boolean.

set1 = {7, 10.5, 'Hello', (5, 6, 7), True}
set2= {7, 75, 45, 9}
print("set1 values :-", set1)
set1.add('Woohoo') #will add this randomnly anywhere in the set
print("Value on adding new value to the data set is : ", set1)
print("_"*50)
set1.remove('Hello')
print("If we remove a value 'Hello' from set : -", set1)
set1.discard(False)
print("IF we remove a value which doesn't not exist in the set,we use discard method."
       "and we won't see error message unline set.remove :", set1)

print("_"*50)

# Use of union, update,difference, symmetric difference and intersection methods
setA = { 8, 9, 'z', 'x', 12}
setB = {'x', 'y', 'z', 8, 12}
print("value of setA are :", setA)
print("value of setB are :", setB)
setA.union(setB)
print("To add / concatenate 2 sets, we use union method :", setA)
setA.update(setB)
print("To update value of one set to another, we use update method :", setA)
setA.difference(setB)
print("To find the difference/ remove common between 2 methods and only print unique #, we use difference method", setA)
setA.symmetric_difference(setB)
print("To find the difference/ remove common between 2 methods and only print unique #, we use difference method", setA)
setA.intersection(setB)
print("The intersection method will help find common values btn 2 sets : -", setA)