def handle_exception():
    try:
        a = 10
        b = "Hello"
        print(a+b)
    except Exception as e:
        print(e)
handle_exception()
print("good morning")