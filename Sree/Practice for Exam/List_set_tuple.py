#######  Funtions ############

l1=[3,6,33,200,100,50,1,2,6,6,6,]

print(max(l1))
print(min(l1))
print(len(l1))
print(list(reversed(l1)))
print(list(sorted(l1)))
print(list(sorted(l1,reverse=True)))
print(sum(l1))
### Methods       ####################
l2=[2,2,22,2,2,]
l3=[3,3,3,3,3,]
l2.append(l3)
print("append",l2)
l2.insert(2,50)
print('insert:',l2)# inserts 50 at index 2
l1.extend((4,6,8,9))
print('extend',l1)# extend with tuple
l1.extend("acved")
print('extend with string',l1)
set={5,6,7}
l3.extend(set)
print('extend with set',l3)
l4=[1,1,1,1,]
#####################################
dic= {"a": 10, "b": 20}  #       dictionaries only iterate over their keys.
l4.extend(dic)
l4.extend(dic.items())
print('extend with dic',l4)
###################################
l5=[5,5,5,5]
l6=[6,6,6,6]
print('add method',l5.__add__(l6))
print('+ method',l5+l6)
################################
l7=[8,7,79,99,]
l7.remove(99)
print('removed',l7)
print('pop method',l7.pop(0))
print('after remove & pop method',l7)
l8=l7.pop()
print('after 2nd pop method',l8)
#########################
l9=[6,6,8,8,0,0,]
l9.clear()
print('cleared:',l9)
################################
l10=[1,1,4,6,9,33,890,23]
l10.sort()
print('sort method',l10)
l10.sort(reverse=True)
print('sort met with decendeing order',l10)
##################### copy   #############
l11=[4,4,4,44]
l12=l11
l11.append(100)
l12.append('sree')
print('copy method',l11)
print('copy method',l12)
   ## Deep copy########
l13=[9,9,9,9,9]
l14=l13.copy()
l13.append(100)
l14.append('string')
print('deep copy l13:',l13)
print('deep copy',l14)
############################################
print("_" * 50)
# loop to get value with indexing
l15=[5,7,8,3,2,1]
l16= len(l15)
for i in range(l16):
    print(i,"index=",l15[i])
##################################
for i in range(-l16,0,1):
    print(i,"index=",l15[i])
######################## Slicing in the list ##############################
l17=[9,8,7,6,5,4,3,2,2,1]
print('1',l17[0:5])
print('2',l17[6])
print('3',l17[::-1])
print('4',l17[5:9:1])
print('5',l17[8:-1])
print('6',l17[-1:-10:-1])


D1 = {'a': 19, 'b': 20, 'c': 21, 'd': 20}
l1 = list(D1.items())  # use list(), not l1()

print(l1)
