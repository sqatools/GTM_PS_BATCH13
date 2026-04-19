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


def longest_unique_substring(s):
    res = ""
    for i in range(len(s)):
        temp = ""
        for j in range(i, len(s)):
            if s[j] in temp:
                break
            temp += s[j]
        if len(temp) > len(res):
            res = temp
    return res

print(longest_unique_substring("abcabcbb"))


rows = 4
for i in range(1, rows + 1):
    # Print spaces
    print(" " * (rows - i), end="")
    # Print numbers
    for j in range(1, i + 1):
        print(j, end="   ")
    print()

s = "madam"
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")





