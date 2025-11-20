def greetings():
    return "Good Morning"
    return "Good Evening"

def gen_greeting():
   yield "Good Morning"
   yield "Good Evening"
   yield "Good Night"
val=greetings()
print(val)

val=gen_greeting()
#print(val)
#print(next(val))
#print(next(val))
#print(next(val))
for data in val:
    print(data)


###Lambda ### :This is anonymous function that has not have body.
func =lambda x,y: x+y
print(func(1,2))
func2=lambda a: a**2
print(func2(4))


#Map , Filter , Reduce
#
def Square(a):
    return a**2


list1=[1,2,3]
result=list(map( Square,list1))
print(result)

result2=list(map(lambda a: a**2, list1))
print(result2)

### Filter #### :Filter generate the output on the basic expected condition only
list2=[1,2,3,4,5,6]
filter_result=list(filter(lambda x:x%2==0, list2))
print(filter_result)

### Reduce ### :reduce generate only single value from list of input
from functools import reduce
list3=[1,2,3,4,5,6]
output=reduce(lambda x,y:x*y,list3)
print(output)



