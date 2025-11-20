def greet():
    return 'Hello World!'

def gen_greet():
    yield 'Hello World!'
    yield 'Good Morning!'
    yield 'Good Afternoon!'

val = greet()
print(val)

val2 = gen_greet()
print(val2)
print(next(val2))
print(next(val2))
#print(next(val2))

for num in val2:
    print(num)