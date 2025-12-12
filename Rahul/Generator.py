
def greetings():
    return "DO Workout"


def gen_greeting():
    yield "Go to GYM"


val = greetings()
print(val)

value = gen_greeting()
print(value)


for data in value:
    print(data)

