set1 = {12,2,3,'Hello',(3,5),False}
print(set1, type(set1))

#Apply loop on set

set2 = {12,2,3,'Hello',(3,5),False}
for val in set2:
    print (val)

#Total count
print('total count :', len(set2))

 #Methods of set

 # Add method : it can be added in random position
set_a ={3,4,5}
set_a.add(20)
print(set_a)

#remove method

#remove data from set - Existing Method -
set_b={4,5,7}
set_b.remove(4)
print(set_b)

#remove data from set - non-Existing Method - for this we will get keyerror :3
'''set_b.remove(3)
print(set_b)
'''
#get the output without getting error in non exsiting method
set_c={43,55,79}
set_c.discard(3)
print(set_c)

#Combined two sets

#Union method =

set_d = {23,45,67}
set_e= {55,10,37}

set_f = set_d.union(set_e)
print(set_f)

#Udate method
set_x ={3,4,6}
set_y ={6,7,8}
set_y.update(set_x)
print(set_x)
print(set_y) # it will update only set_y

set_p ={73,49,60}
set_q ={68,77,98}
set_p.update(set_q)
print(set_p) # - it will update only set_p method

#Difference Method







