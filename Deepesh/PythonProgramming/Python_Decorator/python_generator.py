# Generator helps to manager the system memory and proces huge data one bye obe without over loading the system
# memory.

# normal function
def greetings():
    return "good Morning"
    return "good evening"

# function with generator, it can return value one by one
def gen_greeting():
    yield "Good Morning"
    yield "Good Evening"
    yield "Learning Python"
    yield "Good Afternoon"


val = greetings()
print(val)

value = gen_greeting()
print(value)
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))


for data in value:
    print(data)

print("_"*50)
#################################################
# Lambda :  This anonymous function that does not have body
#
func = lambda x, y: x+y
# x,y : parameter
# x+y : operation

print(func(50, 70))  # 120

func2 = lambda  a: a**2
print(func2(10))  # 100

# Map, Filter , reduce
# Map : map function can apply list of inputs to one single function and generate output.

def sqaure(a):
    return a**2

list1  = [5, 7, 9, 2, 4]
result = list(map(sqaure, list1))
print(result)
# [25, 49, 81, 4, 16]

result2 = list(map(lambda a: a**2, list1))
print("result with lambda :", result2)
# result with lambda : [25, 49, 81, 4, 16]


# Filter : Filter generate the output on the basic expected condition only.
list2 = [6, 8, 2, 9, 12, 13]
filter_result = list(filter(lambda x: x%2==0, list2))
print("filter result :", filter_result)  #  filter result : [6, 8, 2, 12]


# Reduce :  Reduce generate only single value from list of input.
from functools import reduce
list3 = [5, 7, 9, 2, 5, 17]
output = reduce(lambda x, y: x+y, list3)
print("reduce output :", output) # reduce output : 45