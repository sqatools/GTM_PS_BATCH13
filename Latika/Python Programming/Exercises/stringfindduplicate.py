print("Write a python program to remove duplicates word from given list")

str1="latika shalaka sweety sadhna latika sweety"
print("Orignal string is :",str1)

word_list=str1.split(" ")
print(word_list)
result=" "
for word in word_list:
    if word not in result:
        result=result+word+" "
    else:
        continue
    print(result)
print("Final Result is :",result)