print(['rahul', 'Arnold', 9, 99, 34])
print("_"*50)
list_R = ['rahul', 'Arnold', 9, 99, 34]

X5 = list_R.pop()
print("the removed value is :", X5)
print("list_R :", list_R)


X2 = list_R.pop(1)
print("the removed value is :", X2)
print("list_R :", list_R)

print("_"*50)

#shallow copy

list_R = [6, 9, 88, 3]
list_K = list_R
list_K.append('Rahul')
list_R.append('Kumar')

print("list_R :", list_R)
print("list_K :", list_K)


