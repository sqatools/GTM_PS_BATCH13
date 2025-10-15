############## Python Datatypes##############
##########  1) NUMBERS  ############
#1)Integer
num1=20
num2=30
print("value of num1:",num1,type(num1))
print("value of num2:",num2,type(num2))

#2)Float
f1=0.2
f2=56.876543
print("value of f1:",f1,type(f1))
print("value of f2:",f2,type(f2))

#3)Complex
comp1=10+20j
comp2=30j
print("value of comp1:",comp1,type(comp1))
print("value of comp2:",comp2,type(comp2))

######## 2)Strings ################

s1=""
s2="_"
s3="#$%^&*"
s4=''
s5='_'
s6=''''''
s7="' "
s8="Hello"
print("s1:",s1,type(s1))
print("s2:",s2,type(s2))
print("s2*10")
print("s3:",s3,type(s3))
print("s4:",s4,type(s4))
print("s5:",s5,type(s5))
print("s6:",s6,type(s6))
print("s7:",s7,type(s7))
print("s8:",s8,type(s8))

#Positive and Negative indexing

str1= "P Y T H O N"
print("str[0]")
print("str[-4]")

#####  LIST #######
#List is mutable data type

list1=[1,2,4.5,"hello",[2,3],(8,9),{"a":123},True]
print(list1,(type(list1)))
print(list1[4])
print(list1[5][0])

list2=[20,[20,9],True]
print(list2[1])
print(list2[1][0])

####### append -- used to add list##########
list2.append(40)
print(list2)

############### TUPLE ##################
#tuple is immutable
#tup=()

tup1=(4,3,8,'python',[3,7],(8,9),{'a':45})
print(tup1,type(tup1))
print(tup1[0])
print(tup1[4][1])
print(tup1[-1])
print(tup1[-1]['a'])

######### DICTIONARY ###############
# Dict is mutable data type
# dict={'Key':Value}

dict={'a':123,'b':456,'c':324}
print(dict)
print(dict,type(dict))
print(dict['a'])
print(dict['b'])

############# SET #################
#Set is mutable

set1={20,10,7.4,10+20j,"hello",True}
print(set1)
print(set1,type(set1))

############### BOOLEAN ############
var1=100
var2=200
print(var1>var2)
print(var1<var2)
