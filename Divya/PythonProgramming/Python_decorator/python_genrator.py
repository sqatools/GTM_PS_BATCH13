func = lambda x,y: x+y
print(func(10.0,20.0))

func2 = lambda x: x**2
print(func2(30))

list1 = [1,2,3,4,5]
filter_result = list(filter(lambda x:x%2==0, list1))
print("filter_result : ",filter_result)
