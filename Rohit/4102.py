with open ("2ndFiles.txt","r") as f:
    lines = f.read()
    print(len(lines))

with open ("TestFile.txt","w") as f:
    f.write("Hello Good Evening Guys")


st = "a2b3c4d1"
result = ""

for i in range(0,len(st),2):
    char = st[i]
    count = int(st[i+1])
    result += char * count
print(result)



st = "abcabcbb"

unique = ""

for i in st:
    if i not in unique:
        unique += i
print(unique)

rows = 4

for i in range(1,rows+1):
    print(""*(rows-1),end="")

    for j in range(1,i+1):
        print(j,end="  ")

    print()

s = "Hello I am Rohit"

result1 = " ".join(words[::-1] for words in s.split())
print(result1)

str1 = "Gurgaon city is Good"

words = str1.split()

# rearranging words
output = words[0] + " " + words[2] + " " + words[3] + " " + words[1]

print(output)


text = "I Love JAVA Programming"

unique_chars = set(text)

print(unique_chars)