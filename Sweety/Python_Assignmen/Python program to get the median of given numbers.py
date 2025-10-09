# example list of values
values = [10, 20, 30, 40, 50]

# sort the list
values.sort()

# get length of the list
n = len(values)

if n % 2 == 1:
    median_value = values[n // 2]
else:
    median_value = (values[n // 2 - 1] + values[n // 2]) / 2

print(f"The median is: {median_value}")



