# Generator helps to manager the system memory and proces huge data one bye one without over loading the system
# memory.

# normal function
def greetings():
    return "Good Morning"
    return "Good Evening"

val = greetings()
print(val)  #Good Morning

print("-"*50)
###################################################
# function with generator, it can return value one by one (if we want call multiple results at a time)

def gen_greeting():
    yield "Good Morning"
    yield "Good Afternoon"
    yield "Good Evening"
    yield "Good Night"
    yield "Learning Python"

val1 = gen_greeting()
#print(val1)
#print(next(val1)) # Good Morning
#print(next(val1)) # Good Afternoon
#print(next(val1)) # Good Evening
#print(next(val1)) # Good Night
#print(next(val1)) # Learning Python



#If we can to call all results at a time then in one time

for data in val1:
    print(data)
'''
Good Morning
Good Afternoon
Good Evening
Good Night
Learning Python
'''