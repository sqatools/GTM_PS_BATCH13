a={1:'a',2:'b',3:'c',4:'d'}
print(type(a))

b={4:'x',5:'y',6:'z',7:'w'}

a[9]='v'
b[8]='u'
print(a,b)

#loop on dict
for k,v in a.items():
    print(k,v)

# create dict from given string
sent="we are humans"
splitting=sent.split(" ")
print(splitting)
result={}
for i in splitting:
    first=i[0]
    result[first]=i


print(result)

