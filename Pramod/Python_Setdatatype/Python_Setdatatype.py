# Set datatype
set1 = {3,3.5, 'Hello', (3,5,6), True}
print(set1, type(set1))

#Duplicate datatype
set2 = {3,3.5, 'Hello', (3,5,6), True,3,3.5, 'Hello', (3,5,6), True}
print(set2, type(set2))

#set2 = {3,3.5, 'Hello', (3,5,6), True, [3,5,7]}
#print(set2, type(set2))
# TypeError: unhashable type: 'list'
print("_"*50)

# Apply loop on set
set3 = {3,3.5, 'Hello', (3,5,6), True}
for val in set3:
    print(val)

""" 
True
3
3.5
(3,5,6)
Hello
"""

print("total values:", len(set3))
#Total Values : 5
########################Sets Methods ###################
#Add methode: add data to the set.
set_a = {4,6,8,12}

# remove existing value
set_b = {4,6,8,12,10}

# Remove Non-Existing value
set_b.remove(10)
print(set_a)
print(set_b)