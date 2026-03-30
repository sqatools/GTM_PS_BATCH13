rows = 4
for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print numbers
    for j in range(1, i + 1):
        print(j, end="   ")
    print()

s = "automation"
vowels = "aeiou"
count = 0

for ch in s:
    if ch in vowels:
        count += 1

print(count)
