str1="dexter karall1"
str2="""Dexter Krall2"""
str3='''DEXTER KRALL3'''
str4=100

print(str1,str2,str3)
print("small letters->"+str1+"camle case->"+str2+"capital leters->"+str3+"number"+str(str4))
print(f"a{str1}b{str2}") #fstring
print("a{}b{}".format(str1,str2)) #format method

str="dwijesh badari"
print(str[0:7]+"  "+str[-1:-7:-1])
print(str[0:7])
print(str[8:14])
print(str[:8])
print(str[1:])
print(str[:])