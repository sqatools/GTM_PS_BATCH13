def greetings():
    return "good Morning"
    return "good evening"

def gen_greeting():
    yield "Good Morning"
    yield "Good Afternoon"
    yield "Good Evening"
    yield "Good Night"

val = greetings()
print