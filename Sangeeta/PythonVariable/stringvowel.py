#Write a prg. to count vowels from string

str3 = "good morning, hope you are doing good!"
vowels = "aeiouAEIOU"
count = 0 #Initially keep it o , we are initializing the counter.this will increase as the loop runs
for char in str3:
    print(char)
    if char in vowels:
        count += 1
    else:
        continue

    print("Total vowels :", count)