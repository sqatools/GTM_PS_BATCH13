import time

import requests
"""
text = "I Love JAVA Programming"
output = set(text)
print(output)

str1 = "Gurgaon city is Good"
word = str1.split()
output = word[0]+" "+word[2]+" "+word[3]+" "+word[1]
print(output)


Input = "a2b3c4d1"
result= ""

for i in range(0,len(Input),2):
    char = Input[i]
    count = int(Input[i+1])
    result += char*count
print(result)

Input ="abcabcbb"
result = ""
for i in Input:
    if i not in result:
        result += i
print(result)

rows = 4

for i in range(1,rows+1):
    print(""*(rows-1),end=" ")
    for j in range(1,i+1):
        print(j,end= " ")
    print()

s = "python"
result = " "
for ch in s:
    result = ch + result
print(result)

s = "Hello I am Rohit"
output = " ".join(word[::-1] for word in s.split())
print(output)


s = "madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("Not palindrome")


lst = [1, 2, 3, 2, 4, 1]
duplicate = [x for x in lst if lst.count(x)>1]
print(duplicate)


lst = [1, 2, 2, 3, 4, 4,5]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)

lst = [10, 5, 20, 8]

max_num = lst[0]
for i in lst:
    if i > max_num:
        max_num = i
        print(max_num)

maximum = max(lst)
minimum = min(lst)
print(maximum)
print(minimum)


s = "automation"
char_count= {}

for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1
print(char_count)

num= 7
if num >1:
    for i in range(2,num):
        if num%i==0:
            print("Not Prime")
        else:
            print("prime")

n=5
a,b = 0,1
for _ in range(n):
    print(a,end=" ")
    a, b = b, a+b

with open ("2ndFiles.txt","r") as f:
    line = f.read()
    print(len(line))

with open ("2ndFiles.txt","w") as f:
    f.write("Hello")

s = "automation"
vowels = "aeiou"
count = 0
for i in s:
    if i in vowels:
        count += 1
print("count :", count)


input_list = ['apple', 'banana', 'apple', 'pear', 'banana', 'apple']

output = {}

for index, value in enumerate(input_list):
    if value not in output:
        output[value] = []
    output[value].append(index)

print(output)

nums = []
for i in range(5):
    n = int(input(f"Enter number {i+1}:"))
    nums.append(n)
nums = list(set(nums))
nums.sort(reverse=True)
print("2nd highest value :", nums[1])



def test_login_api():

    url = "https://www.checkoutx.com/endpoint"

    payload = {
        "name": "client",
        "password": "xyz"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200

"""
count = 0
with open("2ndFiles.txt","r") as f:
    lines = f.read()
    print(len(lines))

    for i in lines:
        count +=1
    print("counts:",count)

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
"""
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if not checkbox.is_selected():
        checkbox.click()
        time.sleep(2)
"""
row  = driver.find_element(By.XPATH,"//td[text()='Internet Explorer']//parent::tr")
cols = row.find_elements(By.TAG_NAME,"td")

print("CPU:", cols[2].text)


driver.close()