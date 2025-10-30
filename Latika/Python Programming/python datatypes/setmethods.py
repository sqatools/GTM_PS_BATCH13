set1={3,5.6,'hello',(3,6,8),True}
print(set1,type(set1))

# apply loop
set2={3,5.6,'hello',(3,6,8),True}
for val in set2:
    print(val)
print("total count of set is:",len(set2))

# Set Methods
# Add Method
set_a={4,7,9,10}
set_a.add(100)
print(set_a)

# remove method
set_b={4,7,8,10}
set_b.remove(4)
print(set_b)

# Discard method
#
set_c={4,6,9,12,50}
set_c.discard(50)
print(set_c)

set_c.discard(100)

# Update method
set_A={3,6,9}
set_B={'a','b','c'}
set_C=set_A.union(set_B)
print("set_C is :",set_C)

#Update Method
set_x={6,8,9}
set_y={6,2,1}
set_y.update(set_x)
print(set_y)

# Difference Method

set_x={3,7,9,10,'a','b','c'}
set_y={'a','b','c','p','q'}

result1=set_x.difference(set_y)
print(result1)

result2=set_y.difference(set_x)
print(result2)

# Symmetric difference
set_p={3,7,9,10,'a','b','c'}
set_q={'a','b','c','p','q'}
result=set_p.symmetric_difference(set_q)
print(result)

# Intersection method

set_p={3,7,9,10,'a','b','c'}
set_q={'a','b','c','p','q'}
result_i=set_p.intersection(set_q)
print(result_i)



