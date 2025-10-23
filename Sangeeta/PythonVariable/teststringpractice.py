# String Concatenation

name = 'Rohan'
Age = 25
city = 'Mumbai'

Result1 = "My name is " + name + " and age is " + str(Age) + " I live in"+city
print(Result1)

# format method
Result2 = "My name is {} and age is {}, I live in {}".format(name,Age,city)
print(Result2)

# fstring method
Result3 = f"My name is {name} and age is {Age}, I live in {city}"
print(Result3)
