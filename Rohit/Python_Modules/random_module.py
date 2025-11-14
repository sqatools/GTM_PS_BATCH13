import random

# Generate random values : Values will get change very time
result = random.randint(1,20)
print("result :", result) # 19

# Generate random values from list of : Values will get change very time
result1= random.choice([2,4,5,45,77])
print("Random values from list :", result1) #2

# shuffle value from given list : Values will get change very time
list = ['a','p',123,55,'f']
random.shuffle(list)
print(list)  # [55, 123, 'f', 'p', 'a']