import random
# generate random number
result1 = random.randint(1,20)
print("Result1:",result1)
# get random value from list of data
result2=random.choice([4,5,9,2,77,9])
print("Result2 ran choice:",result2)
# shuffle value from given list
list = [3,9,12,55,77,33]
random.shuffle(list)
print(list)
