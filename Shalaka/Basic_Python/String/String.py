str1 ="Hello Shalaka Beloshe"

print(str1[:2])

print(str1[:])
print(str1 [-7:-1])
print (str1[:6:-1])

#STRING Methods

#REVERSE STring

str2 = "Hi My name is shalaka"
print('reverse name:', str2[::-1])

#Upper & Lower case method

str3 = "We are learning python"
print("Uppercase :", str3.upper())
print("Lowercase :", str3.lower())

#isupper & islower case : returning the boolean value
str4 = "We are learning python"
str5 = "HEELO"
str6 = "python"

print("str4 :", str4.isupper(), str4.islower())
print("str5 :", str5.isupper())
print("str6 :", str6.islower())

#SWAPcase method : lower to upper & upper to lower
str7= "wE arE lEarnIng pYthOn"
print ("swap:", str7.swapcase())


#Capatalized method : first char will be upper and rest will be lower

str8= "wE arE lEarnIng pYthOn"
print ("Capitalize:", str8.capitalize())

#Title Method : Covert each first word in upper case
str9= "wE arE lEarnIng pYthOn"
print ("Tile:", str9.title())

#Count Method : return the total count of any character / substrin of any string
# count of char
str10 = "We are learning python, and doing good"
print ("count of a :", str10.count('a'))
# count of substring
print ("count of ing :", str10.count('ing'))

#index method : method return the index position of any char
str11 = "Good morning, Hope you are doing good"
print("index of hope :",str11.index("Hope"))
print("index of 0:", str11.index("o"))


#Split Method : this method spilit string  from given char / space / comma & return list of words
str13 = "Good morning Hope you are doing good"
result1 = str13.split(" ")
print (result1)


str14 = "Good morning, Hope you, are doing good"
result2 = str14.split(',')
print (result2)





