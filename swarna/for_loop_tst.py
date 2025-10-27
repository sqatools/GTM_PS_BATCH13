


# There's another kind of loop — the `for` loop.

# It looks like this:

for sita in ["a", "b", "c"]:
  print(f"This letter is {sita}")

for rama in range(0, 10):
    print(f"This number is {rama}")

number = 0
while number < 10:
    print(f"This number is {number}")
    number = number + 1


print(1)
print(2)

"""
# range(start, end, step value)
->  Output of the range will include start value and exclude the end value.
->  Output will show value as per the step value from start to end.
->  default start value is zero and default step value is 1
    range(10)  ->  range(0, 10, 1)
    range(3, 10) -> range(3, 10, 1)
->  start value, end value and step value could be +ve or -ve
"""

print("_"*40)
for i in range(1, 10, 1):
    print(i)