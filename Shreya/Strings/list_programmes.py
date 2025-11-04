##################33programmes##########################

#removing duplicates from the list:
print("_"*40)
list_1= ["shreya", "Ankit", "Darshani", "Ravi", "shreya"]
result_1=["Prisha"]
for val in list_1:
    if val not in result_1:

        result_1.append(val)
    else:
        continue
print("new list:", result_1)
#print("_"*40)
#moving values in left and right to the positive and negative values:
print("_"*50)
list_2=[33,-9,45,76,-1,2,-8]
pos_list=[]
neg_list=[]

for val in list_2:
    if val > 0:
     pos_list.append(val)
    else:
     neg_list.append(val)

result_2 = neg_list + pos_list
print("result_2 :", result_2)
sort_list = list(sorted(result_2))
print("sorted list :", sort_list)
print("_"*40)
#by using min and max functions :
list_a=[1,2,3,44,78.99,45]
print("max_value :",max(list_a))
print("min_value :",min(list_a))
print("sum of min and max:", sum(list_a))