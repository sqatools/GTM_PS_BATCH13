str1="dexter karall1"
str2="""Dexter Krall2"""
str3='''DEXTER KRALL3'''
str4=100

print(str1,str2,str3)
print("small letters->"+str1+"camle case->"+str2+"capital leters->"+str3+"number"+str(str4))
print(f"a{str1}b{str2}") #fstring
print("a{}b{}".format(str1,str2)) #format method

str="dwijesh badari"
print(str[0:7]+"  "+str[-1:-7:-1])#dwijesh  iradab
print(str[0:7])
print(str[8:14])
print(str[:8])
print(str[1:])
print(str[:])

print("upper", str.upper())
print("lower" ,str3.lower())
print("isupper,islower" ,str1.isupper(),str3.islower())
print("conver upper to lowerand lower to upper",str2.swapcase())
print("convert lower to upper",str1.capitalize())
print("camle case",str.title())
print("count",str.count("a"))
print("index of badri",str.index("badari"))
split=str.split(" a")# it will split the words in the sentence from the given referance in the split function
replace=str.replace("badari","b")

str5=" i am learning  "
str6="""python"""
str7=["abc","abcd","abcde","abcdef"]

res1="abc".join(str6)
print(res1)
res2=" ". join(str7)
print(res2)
print("strip is for removing space",str5.strip())
