
"""properties of list:
1) immutable datatype
2)any datatypes we can add under square brackets
3)positive negative indexing
"""
list_1=[22,'Shreya',8.8,{'key':'value'},False,[1,2,3,4]]
print(list_1,type(list_1))
print('_'*40)
########################################3slicing###########################
print(list_1[3])
print(list_1[::-1])
###############################################loop#######################
list_1=[2,4,6,7,5,22,89]
output=[]
for val in list_1:
    if val% 2 ==0:
        output.append(val)
    else:
        continue
        print("output:", output)

      print('_'*40)

