# Lambda :  This anonymous function that does not have body


func = lambda x, y: x+y
# x,y : parameter
# x+y : operation
print(func(10,20)) # 30

print("-"*50)
############################################
func1 = lambda a: a**2
print(func1(5)) # 25

print("-"*50)

#########################################################
# Map, Filter , reduce
# Map : map function can apply list of inputs to one single function and generate output.

def square(a):
    return a**2

list1 = [3,4,7,8,5]

result = list(map(square , list1))
print(result) # [9, 16, 49, 64, 25]

# with lambda function
result1 = list(map(lambda a: a**2, list1))
print(result1) # [9, 16, 49, 64, 25]

print("-"*50)

##########################################
# Filter : Filter generate the output on the basic expected condition only.

list3 = [2,5,8,12,19,24]
result2 = list(filter(lambda x: x%2==0, list3))
print("Even number :",result2) # Even number : [2, 8, 12, 24]

print("-"*50)
#######################################################
# Reduce :  Reduce generate only single value from list of input.
from functools import reduce

list4 = [3,5,7,9,3,10]
output = reduce(lambda x,y: x+y, list4)
print("Sum of list :", output) #  Sum of list : 37