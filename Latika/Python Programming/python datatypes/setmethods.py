set1={3,5.6,'hello',(3,6,8),True}
print(set1,type(set1))

# apply loop
set2={3,5.6,'hello',(3,6,8),True}
for val in set2:
    print(val)
print("total count of set is:",len(set2))

print()
print("."*100)

# Set Methods
# Add Method
set_a={4,7,9,10}
set_a.add(100)
print("After addition result is",set_a)

print()
print("."*100)

# remove method
set_b={4,7,8,10}
set_b.remove(4)
print("After removing 4 :",set_b)

print()
print("."*100)

# Discard method
#
set_c={4,6,9,12,50}
set_c.discard(50)
print("After discarding result is: ",set_c)
set_c.discard(100)
print(set_c)

print()
print("."*100)

# Update method
set_A={3,6,9}
set_B={'a','b','c'}
set_C=set_A.union(set_B)
print("Updated set_C is :",set_C)

print()
print("."*100)

#Update Method
set_x={6,8,9}
set_y={6,2,1}
set_y.update(set_x)
print("After updating the result is",set_y)


print()
print("."*100)

# Difference Method

set_x={3,7,9,10,'a','b','c'}
set_y={'a','b','c','p','q'}

result1=set_x.difference(set_y)
print("Result of difference method",result1)

result2=set_y.difference(set_x)
print(result2)

print()
print("."*100)

# Symmetric difference
set_p={3,7,9,10,'a','b','c'}
set_q={'a','b','c','p','q'}
result=set_p.symmetric_difference(set_q)
print("result of symmetric difference is",result)

print()
print("."*100)

# Intersection method

set_p={3,7,9,10,'a','b','c'}
set_q={'a','b','c','p','q'}
result_i=set_p.intersection(set_q)
print("result of intersection method is:",result_i)



